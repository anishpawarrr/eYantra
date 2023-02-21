import streamlit as st
import pyrebase as pb
import impvari

def checklogin(mail, password):
    fb = pb.initialize_app(impvari.config)
    auth = fb.auth()
    try:
        user = auth.sign_in_with_email_and_password(mail,password)
        if auth.send_email_verification(user['idToken']):
            return True
    except:
        return False

def log():
    if 'logbool' not in st.session_state:
        st.session_state['logbool'] = False
    if 'mail' not in st.session_state:
        st.session_state['mail'] = ''
    if 'pw' not in st.session_state:
        st.session_state['pw']=''

    if not st.session_state['logbool']:
        with st.form('login form'):
            st.subheader('Enter Login credentials')
            st.session_state['mail'] = st.text_input("Enter mail")
            st.session_state['pw'] = st.text_input('Enter passwowrd')
            fsb = st.form_submit_button("Login")
            st.session_state['logbool'] = True
            # if fsb:
            #     st.form_submit_button('tp')
                # st.session_state['logbool'] = True
    else:
        st.write(st.session_state['mail'])
        st.write(st.session_state['pw'])
        # b = checklogin(st.session_state['mail'], st.session_state['pw'])
        # if b:
        #     st.write("Logged in ")
        # else:
        #     st.write('Wrong cred')
        #     st.write(st.session_state['mail'])
        #     st.write(st.session_state['pw'])
        #     st.write('111')