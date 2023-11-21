import serial
import time
from firebase_admin import credentials
from firebase_admin import db
import firebase_admin


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

while True:
    inp = str(ser.readline().decode("utf-8"))
    if inp == "0" or inp == "1":
        mb_button = str(ser.readline().decode("utf-8"))
        mb_button = mb_button.replace("\r\n","")
        print(mb_button)
        if mb_button.isdigit():
            temperature_log_ref.update({str(int(time.time())):{"Temperature":mb_button,"Location":source}})
        
    else:
        mb_temperature = inp
        mb_temperature = mb_temperature.replace(" ","")
        mb_temperature = mb_temperature.replace("\r\n","")
        print(mb_temperature)
        if mb_temperature.isdigit():
            temperature_log_ref.update({str(int(time.time())):{"Temperature":mb_temperature,"Location":source}})
        else:
            print("Check data source")