from sense_hat import SenseHat
import firebase_admin
from firebase_admin import credentials, firestore

# Constants
COLLECTION = 'raspberry'
DOCUMENT = 'student_pi'

# Firebase
cred = credentials.Certificate("../config/iotlabo3-robin-firebase-adminsdk-k0azw-6ff0bab77e.json")
firebase_admin.initialize_app(cred)

# Sensehat
sense = SenseHat()
sense.set_imu_config(False, False, False)
sense.clear()

def update_sensehat(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        doc_readable = doc.to_dict()
        print(doc_readable)

# Connect firestore
db = firestore.client()
pi_ref = db.collection(COLLECTION).document(DOCUMENT)
pi_watch = pi_ref.on_snapshot(update_sensehat)

# App
while True:
    pass