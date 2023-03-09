import datetime
import firebase_admin
from firebase_admin import db, credentials

cred = credentials.Certificate("serviceaccountKey.json")
app = firebase_admin.initialize_app(cred)