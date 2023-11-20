import time
from firebase_admin import credentials
from firebase_admin import db
import firebase_admin
def something_changed(response):
    print(response.event_type)
    print(response.data)

cred = credentials.Certificate("C:/Users/Nandi/zene/school/info/firebase/asd1-2088b-firebase-adminsdk-86y24-da4df843ef.json")
firebase_admin.initialize_app(cred,{"databaseURL": "https://asd1-2088b-default-rtdb.europe-west1.firebasedatabase.app"})

ref = db.reference().child("temperature_log")
my_ref = ref.listen(something_changed)









