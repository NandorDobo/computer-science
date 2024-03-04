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
ref.child("small_rest_preference").set(10)
ref = db.reference("/user/preferences")
ref.child("study_time").set(20)
ref.child("sport_time").set(20)
ref = db.reference("/user/times")
ref.child("study_time").set(40)
ref.child("sport_time").set(40)
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

def today_times(remaining):
    remaining_time = 0
    ref = db.reference('/user/times/study_time')
    study_time = int(ref.get())
    remaining -= study_time
    ref = db.reference('/user/remaining_times')
    ref.child("study_time").set(study_time)
    
    ref = db.reference('/user/times/sport_time')
    times["sport_time"] = int(ref.get())
    remaining -= times["sport_time"]
    ref = db.reference('/user/remaining_times')
    ref.child("sport_time").set(times["sport_time"])
    
    
    ref = db.reference('/user/times')
    times["rest_time"] = remaining

    return times 
times = {}
times.update(today_times(remaining))
print(times)

def start(times):
    name = input("What is your username?")
    print("What do you want to do first?")
    prev = input("study,phisical activity,rest")
    working_values = {}
    working_values["name"] = name
    working_values["prev"] = prev
    return working_values
working_values = start(times)

    
    
    
    
def send(working_values,times):
    if(working_values["prev"] == "rest"):
        ref = db.reference('/' +working_values["name"]+ "/small_rest_preference")
        
    else:
        ref = db.reference('/' +working_values["name"]+ "/times/" +working_values["prev"]+ "_time")
        
    task_time = ref.get()
    print(task_time)
    ser.write((str(task_time)+",").encode("utf-8"))
send(working_values,times)

def receive():
    while True:
        rec = ser.readline().decode('utf-8').strip()
        if (rec != ""):
            break
        
    received_values = rec.split(",")
    return received_values
print(receive())
    



# ser.write("120,".encode("utf-8"))










