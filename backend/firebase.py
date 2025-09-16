import firebase_admin
from firebase_admin import credentials, firestore, storage

cred = credentials.Certificate("serviceAccountKey.json")  # descarga de Firebase
firebase_admin.initialize_app(cred, {
    "storageBucket": "TU_BUCKET.appspot.com"
})

db = firestore.client()
bucket = storage.bucket()
