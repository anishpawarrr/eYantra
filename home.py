import datetime
import streamlit as st
import streamlit_option_menu as om
import pyrebase as pb
import impvari
from firebase_admin import db, credentials
import firebase_admin
# import login



st.set_page_config(page_title= "VAXER", page_icon='bi bi-activity', layout= 'wide', initial_sidebar_state='expanded')



cred = credentials.Certificate("serviceaccountKey.json")
# app = firebase_admin.initialize_app(cred)
# cred = credentials.Certificate("serviceaccountKey.json")
# app = firebase_admin.initialize_app(cred)

def caldate(dob):
    dob = datetime.datetime.strptime(dob, '%Y-%m-%d')
    vac1date = dob + datetime.timedelta(days=42)
    vac2date = dob + datetime.timedelta(days=70)
    vac3date = dob + datetime.timedelta(days=98)
    return vac1date.date(), vac2date.date(), vac3date.date()

def checklogg(ml, pw):
    fb = pb.initialize_app(impvari.config)
    auth = fb.auth()
    try:
        auth.sign_in_with_email_and_password(ml, pw)
        return True, ml.replace('.', '"')
    except:
        return False, ''

if 'opt' not in st.session_state:
    st.session_state['opt'] = 'Default'
with st.sidebar as sb0:
    opt = om.option_menu(menu_title= 'VAXER', options=['Login', 'Sign up', 'Admin Login', 'Contact Us'], default_index=0, menu_icon='bi bi-layers-fill', icons=['bi bi-door-open', 'bi bi-person-plus', 'bi bi-person-circle', 'bi bi-telephone'])
    st.session_state['opt'] = opt
if st.session_state['opt'] == 'Default':
    #home
    st.write("Home")
elif st.session_state['opt'] == 'Login':
    # login
    # st.write("Login")
    if 'showform' not in st.session_state:
        st.session_state['showform'] = True
    if 'stri' not in st.session_state:
        st.session_state['stri'] = ''
    if st.session_state['showform']:
        ml = st.text_input('Enter mail')
        pw = st.text_input('Enter password', type='password')
        b = st.button('Login')
        if b:
            logbool, st.session_state['stri'] = checklogg(ml, pw)
            # st.button('Verify you are not robot')
            # st.session_state['showform'] = False
            if logbool:
                st.session_state['showform'] = False
                st.write('Logged in successfully')
                # app = firebase_admin.initialize_app(cred)
                ref = db.reference(url='https://vaxer-65c87-default-rtdb.asia-southeast1.firebasedatabase.app/')
                uref = ref.child('users')
                udata = uref.child(st.session_state['stri']).get()
                # st.write(udata)
                st.write(f'Dob of child -> {udata["dob"]}')
                # st.write(f'Type of vaccine -> {udata["vactype"]}')
                st.write(f'vaccination date of OPV-1 -> {udata["opv1"]}')
                st.write(f'vaccination date of OPV-2 -> {udata["opv2"]}')
                st.write(f'vaccination date of OPV-3 -> {udata["opv3"]}')
            else:
                st.write('Wrong credentials')


        # with st.form('Enter login credentials'):
        #     st.subheader('Login')
        #     mail = st.text_input('Enter mail id')
        #     pw = st.text_input('Enter password')
        #     # st.write(stri)
        #     st.session_state['showform'] = False
        #     # try:
        #     #     auth.sign_in_with_email_and_password(mail,pw)
        #     #     st.write('Yay')
        #     # except:
        #     #     st.write('OOPs')
        #     fsb = st.form_submit_button("Login")
        #     if fsb:
        #         st.session_state['stri'] = checklogg(mail, pw)

    # st.write(st.session_state['stri'])

elif st.session_state['opt'] == 'Sign up':
    # st.write("Sign up")
    if 'showsu' not in st.session_state:
        st.session_state['showsu'] = True
    if st.session_state['showsu']:
        ml = st.text_input('Enter mail id by which you will login')
        dob = st.date_input("Enter child's birth date")
        dob = str(dob)
        fml = st.text_input("Enter father's mail id")
        fno = st.text_input("Enter father's phone number")
        mml = st.text_input("Enter mother's mail id")
        mno = st.text_input("Enter mother's phone number")
        nm = st.text_input("Enter name of child")
        pw = st.text_input("Enter password", type='password')
        sb = st.button("Create Account")
        if sb:

            st.session_state['showus'] = False
            # cb = st.checkbox("Verify you are human")
            faml = ml.replace('.','"')
            d1, d2, d3 = caldate(dob)
            d1 = str(d1)
            d2 = str(d2)
            d3 = str(d3)
            # st.write(faml)
            # vacdate = '2023-02-20'
            # dob = '2003-05-22'
            # fno = '9146623526'
            # fml = 'anishpurupawar@gmail.com'
            # mno = '9146623526'
            # mml = 'testmailservice2718@gmail.com'
            # type = 'x'
            # cnm = 'name'
            # rstr = 'anishpurupawar@gmyyyycom'
            # nndata = {
            #     rstr: {'vacdate': vacdate, 'dob': dob, 'fno': fno, 'fml': fml, 'mno': mno, 'mml': mml, 'vactype': type,
            #            'name': cnm}}
            # nndata = {fml: {'vacdate': dob, 'dob': dob, 'fno': fno, 'fml': fml, 'mno': mno, 'mml': mml, 'vactype': 'x', 'name': nm}}
            # if 'su' not in st.session_state:
            #     st.session_state['su'] = firebase_admin.initialize_app(cred, name='su')
            # app = firebase_admin.initialize_app(cred, name='su')
            ndata = {faml: {'opv1': d1, 'opv2': d2, 'opv3': d3, 'dob': dob, 'fno': fno, 'fml': fml, 'mno': mno, 'mml': mml,'name': nm}}
            ref = db.reference(url='https://vaxer-65c87-default-rtdb.asia-southeast1.firebasedatabase.app/')
            uref = ref.child('users')
            uref.update(ndata)
            # ml = 'xyzz@gmail.com'
            fb = pb.initialize_app(impvari.config)
            auth = fb.auth()
            auth.create_user_with_email_and_password(ml, pw)
            del fb
            del auth
            st.session_state['showsu'] = False
            # bu = st.button('1234')
            st.write('Account created Successfully')

    # signup
elif st.session_state['opt'] == 'Admin Login':
    #  admin
    if 'isadmin' not in st.session_state:
        st.session_state['isadmin'] = False

    adpair = {'admin1': 'pass1', 'admin2': 'pass2'}
    adid = st.text_input('Enter id')
    adpw = st.text_input('Enter password', type='password')
    b = st.button('Login')
    if(b and adpw == adpair[adid]):
        st.session_state['isadmin'] = True

    elif b:
        st.write('Wrong credentials')
    if(st.session_state['isadmin']):
        # f = st.file_uploader("Enter excel sheet")
        file = st.file_uploader("Upload records", type={'xlsx', 'csv'})
        if file is not None:
            st.write("File sent successfully")
    st.write("Admin Login")
elif st.session_state['opt'] == 'Contact Us':
    st.write("Contact Us")
    # contact
