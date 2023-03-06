import streamlit as st
import streamlit_option_menu as om
import pyrebase as pb
import impvari
from firebase_admin import db, credentials
# import firebase_admin
# import login

def checklogg(ml, pw):
    try:
        User = auth.sign_in_with_email_and_password(ml, pw)
        if auth.send_email_verification(User['idToken']):
            return True, ml.replace('.', '"')
    except:
        return False, ''

st.set_page_config(page_title= "VAXER", page_icon='bi bi-activity', layout= 'wide', initial_sidebar_state='expanded')

fb = pb.initialize_app(impvari.config)
auth = fb.auth()

cred = credentials.Certificate("serviceaccountKey.json")

if 'opt' not in st.session_state:
    st.session_state['opt'] = 'Default'
with st.sidebar as sb0:
    opt = om.option_menu(menu_title= 'VAXER', options=['Login', 'Sign up', 'Admin Login', 'Contact Us'], default_index=0, menu_icon='bi bi-layers-fill', icons=['bi bi-door-open', 'bi bi-person-plus', 'bi bi-person-circle', 'bi bi-telephone'])
    st.session_state['opt'] = opt
if st.session_state['opt'] == 'Default':
    st.write("Home")
elif st.session_state['opt'] == 'Login':
    # login
    st.write("Login")
    if 'showform' not in st.session_state:
        st.session_state['showform'] = True
    if 'stri' not in st.session_state:
        st.session_state['stri'] = ''
    if st.session_state['showform']:
        ml = st.text_input('Enter mail')
        pw = st.text_input('Enter password')
        b = st.button('Login')
        if b:
            logbool, st.session_state['stri'] = checklogg(ml, pw)
            st.button('Verify you are not robot')
            if logbool:
                st.session_state['showform'] = False
                st.write('Logged in successfully')
                ref = db.reference(url='https://vaxer-65c87-default-rtdb.asia-southeast1.firebasedatabase.app/')
                uref = ref.child('users')
                udata = uref.child(st.session_state['stri']).get()
                st.write(udata)
                st.write(f'Name of ward -> {udata["nm"]}')
                st.write(f'Dob of child -> {udata["dob"]}')
                st.write(f'Type of vaccine -> {udata["vactype"]}')
                st.write(f'vaccination date -> {udata["vacdate"]}')
            else:
                st.write('Wrong credentials')

elif st.session_state['opt'] == 'Sign up':
    st.write("Sign up")
    if 'showsu' not in st.session_state:
        st.session_state['showsu'] = True
    if st.session_state['showsu']:
        ml = st.text_input('Enter mail id by which you will login(father/mother)')
        pw = st.text_input("Enter password")
        sb = st.button("Create Account")
        if sb:
            st.session_state['showsu'] = False  # Change: showus -> showsu
            cb = st.checkbox("Verify you are human")
            u = auth.create_user_with_email_and_password(ml, pw)
            auth.send_email_verification(u['idToken'])
            st.session_state['showsu'] = False
            bu = st.button('1234')
            st.write('Account created Successfully')
