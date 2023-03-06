import pyrebase
import firebase_admin
from firebase_admin import credentials, db
from firebase_admin import firestore


cred = credentials.Certificate("serviceaccountKey.json")
app = firebase_admin.initialize_app(cred)
# {'databaseURL':'https://vaxer-65c87-default-rtdb.asia-southeast1.firebasedatabase.app/' }

#
# config = {
#     'apiKey': "AIzaSyABgU_gESfJR9B8GeWAUTAzkThcwEhgykM",
#     'authDomain': "vaxer-65c87.firebaseapp.com",
#     'projectId': "vaxer-65c87",
#     'storageBucket': "vaxer-65c87.appspot.com",
#     'messagingSenderId': "1039442241546",
#     'appId': "1:1039442241546:web:99f927902583b2f1e957f3",
#     'measurementId': "G-TEQSLX0RHP",
#     'databaseURL':''
# }


# fb = pyrebase.initialize_app(config)
#
# auth = fb.auth()
#
# auth.sign_in_with_email_and_password('1234@mail.com','123456')
# print('sdfgh')
# # auth.send_email_verification(user['idToken'])

# auth.create_user_with_email_and_password(m,pw)


#db
ml = '<anishpurupawar@gmail.com>'
vacdate = '2023-02-20'
dob = '2003-05-22'
fno = '9146623526'
fml = 'anishpurupawar@gmail.com'
mno = '9146623526'
mml = 'testmailservice2718@gmail.com'
type = 'x'
cnm = 'name'
rstr = 'anishpurupawar@gmailllcom'
ndata = {rstr: {'vacdate': vacdate, 'dob': dob, 'fno': fno, 'fml': fml, 'mno': mno, 'mml': mml, 'vactype': type, 'name': cnm}}
# ndata = {str(mno): {'3':ml, '5': '6'}}





# reading db
ref = db.reference(url='https://vaxer-65c87-default-rtdb.asia-southeast1.firebasedatabase.app/')
fbdata = ref.get()
print(fbdata)
# usersref = ref.child('Users').get()
# print(usersref['u1'])

# creating, updating database
# ref = db.reference(url='https://vaxer-65c87-default-rtdb.asia-southeast1.firebasedatabase.app/')
# uref = ref.child('users')
# uref.update(ndata)

# accessing db
# ref = db.reference(url='https://vaxer-65c87-default-rtdb.asia-southeast1.firebasedatabase.app/')
# uref = ref.child('Users')
# udata = uref.get()
# print(type(udata))
# jo = json.dumps(udata)
# print(udata['Anish'])

# sending query
# ref = db.reference(url='https://vaxer-65c87-default-rtdb.asia-southeast1.firebasedatabase.app/')
# uref = ref.child('Users')
# urefdata = uref.get()
# reqml = uref.order_by_child('ml').equal_to('anishpurupawar@gmail.com').get()
# l = []
# for i in reqml:
#     l.append(urefdata[i])
# for i in l:
#     print(i['nm'], i['ml'])