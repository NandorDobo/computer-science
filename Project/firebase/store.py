import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

cred = credentials.Certificate("C:/Users/22NDobo.ACC/info/Project/firebase/project-efc51-firebase-adminsdk-zp4rw-d8b40054e4.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://project-efc51-default-rtdb.europe-west1.firebasedatabase.app'
})

ref = db.reference("/")

#write
# ref.child("user").set({
#     "resttime" : 40
#     })

#Read
# ref = db.reference('/user/resttime')
# snapshot = ref.get()
# print(snapshot)


def rtime():
    now = datetime.now()
    hour = now.hour
    minutes = now.minute
    remaining = (22-hour)*60-minutes
    return remaining
remaining = rtime()
print(remaining)

def basetimes()
    ref = db.reference('/user/rest_time')
    rest_time = ref.get()
    ref = db.reference('/user/sport_time')
    sport_time = ref.get()
    ref = db.reference('/user/small_rest_preference')
    small_rest_preference = ref.get()
    remaining -= rest_time 
    remaining -= sport_time
    small_rest = small_rest_preference*remaining
    remaining -= small_rest
    study_time = remaining










