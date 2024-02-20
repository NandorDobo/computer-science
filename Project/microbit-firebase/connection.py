import serial
import time
from firebase import credentials
from firebase import db
import firebase


ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM5"
ser.open()

cred = credentials.Certificate("C:/Users/22NDobo.ACC/CS/microbit/microbit-firebase/asd1-2088b-firebase-adminsdk-86y24-ffb7c7f69c.json")
firebase_admin.initialize_app(cred,{"databaseURL": "https://asd1-2088b-default-rtdb.europe-west1.firebasedatabase.app"})
ref = db.reference()
ref.update({"temperature_log":""})
temperature_log_ref = ref.child("temperature_log")
source = input("Please input the source of this data: ")

