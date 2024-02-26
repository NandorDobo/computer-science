import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
import serial
from serial.tools.list_ports import comports

PID_MICROBIT = 516
VID_MICROBIT = 3368
TIMEOUT = 0.1
 
def find_comport(pid, vid, baud):
    #list_ports = serial.tools.list_ports.comports()
    ''' return a serial port '''
    ser_port = serial.Serial(timeout=TIMEOUT)
    ser_port.baudrate = baud
    ports = serial.tools.list_ports.comports()
    print('scanning ports')
    for p in ports:
        if (p.pid == pid) and (p.vid == vid):
            print('found target device pid: {} vid: {} port: {}'.format(p.pid, p.vid, p.device))
            ser_port.port = str(p.device)
            return ser_port
    return None
 
ser = find_comport(PID_MICROBIT, VID_MICROBIT, 115200)
if not ser:
    print('microbit not found')
else:    
    ser.open()
    
cred = credentials.Certificate("C:/Users/22NDobo.ACC/info/Project/firebase/project-efc51-firebase-adminsdk-zp4rw-d8b40054e4.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://project-efc51-default-rtdb.europe-west1.firebasedatabase.app'
})

ref = db.reference("/user")

#write
ref.child("rest_time").set(40)
ref.child("sport_time").set(40)
ref.child("small_rest_preference").set(0.8)

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

def basetimes(remaining):
    times = {}
    ref = db.reference('/user/rest_time')
    times["rest_time"] = int(ref.get())
    remaining -= times["rest_time"]
    
    ref = db.reference('/user/sport_time')
    times["sport_time"] = int(ref.get())
    remaining -= times["sport_time"]
    
    ref = db.reference('/user/small_rest_preference') 
    times["small_rest"] = int(ref.get()*remaining)-1
    remaining -= times["small_rest"]
    
    times["study_time"] = remaining
    return times

ser.write("120,".encode("utf-8"))


times = {}
times.update(basetimes(remaining))
print(times)










