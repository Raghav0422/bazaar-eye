# import firebase_admin
# from firebase_admin import credentials, firestore

# cred = credentials.Certificate("serviceAccount.json")
# firebase_admin.initialize_app(cred)

# db = firestore.client()
# print("Firestore connected!")

import firebase_admin
from firebase_admin import credentials, firestore
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
cert_path = os.path.join(base_dir, "serviceAccount.json")

cred = credentials.Certificate(cert_path)
firebase_admin.initialize_app(cred)

db = firestore.client()
print("Firestore connected!")