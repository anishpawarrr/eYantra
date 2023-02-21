from firebase_admin import credentials, db
import pyrebase
import firebase_admin
import impvari
import pandas as pd

# fb = pb.initialize_app(impvari.config)
# auth = firebase_admin.auth()

cred = credentials.Certificate("serviceaccountKey.json")
app = firebase_admin.initialize_app(cred)

f = open('data.csv', 'r')
x=f.readlines()

for i in range(1,len(x)):
    x[i] = x[i].split(',')
    fake = str(x[i][4])
    ndata = {fake.replace('.','"'): {'vacdate': x[i][7], 'dob': x[i][2], 'fno': x[i][0], 'fml': x[i][4], 'mno': x[i][3], 'mml': x[i][5], 'vactype': x[i][6],'name': x[i][6]}}
    # print(ndata)
    ref = db.reference(url='https://vaxer-65c87-default-rtdb.asia-southeast1.firebasedatabase.app/')
    uref = ref.child('users')
    uref.update(ndata)