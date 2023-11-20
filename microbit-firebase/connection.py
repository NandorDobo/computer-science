import serial
import time
from firebase_admin import credentials
from firebase_admin import db
import firebase_admin


ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM3"
ser.open()

cred = credentials.Certificate("C:/Users/Nandi/zene/school/info/firebase/asd1-2088b-firebase-adminsdk-86y24-da4df843ef.json")
firebase_admin.initialize_app(cred,{"databaseURL": "https://asd1-2088b-default-rtdb.europe-west1.firebasedatabase.app"})
ref = db.reference()
ref.update({"temperature_log":""})
temperature_log_ref = ref.child("temperature_log")
source = input("Please input the source of this data: ")

while True:
    mb_temperature = str(ser.readline().decode("utf-8"))
    mb_temperature = mb_temperature.replace(" ","")
    mb_temperature = mb_temperature.replace("\r\n","")
    print(mb_temperature)
    if mb_temperature.isdigit():
        temperature_log_ref.update({str(int(time.time())):{"Temperature":mb_temperature,"Location":source}})
    else:
        print("Check data source")