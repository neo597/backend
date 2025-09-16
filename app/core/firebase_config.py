import os
import firebase_admin
from firebase_admin import credentials, firestore, storage
from dotenv import load_dotenv

# Cargar .env
load_dotenv()

# Variables desde el .env
firebase_config = {
    "type": "service_account",
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace("\\n", "\n"),
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "client_id": os.getenv("FIREBASE_CLIENT_ID"),
    "token_uri": "https://oauth2.googleapis.com/token"
}

# Inicializar Firebase solo una vez
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_config)
    firebase_admin.initialize_app(cred, {
        "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET")
    })

# Firestore y Storage
db = firestore.client()
bucket = storage.bucket()
