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


def today_times(remaining,date):
    ref = db.reference("/user/times/study_time")
    study_time = int(ref.get())
    remaining -= study_time
    ref = db.reference("/user/days/"+date+"/remaining_times")
    ref.child("study_time").set(study_time)
    
    
    ref = db.reference('/user/times/sport_time')
    sport_time = int(ref.get())
    remaining -= sport_time
    ref = db.reference("/user/days/"+date+"/remaining_times")
    ref.child("sport_time").set(sport_time)
    
    
    ref = db.reference('/user/times')
    rest_time = remaining

    return rest_time



def start():
    name = input("What is your username?")
    print("What do you want to do first?")
    prev = input("study,phisical activity,rest")
    working_values = {}
    working_values["name"] = name
    working_values["first"] = prev
    working_values["prev"] = prev
    return working_values


def send(working_values):
    if(working_values["prev"] == "rest"):
        ref = db.reference('/' +working_values["name"]+ "/small_rest_preference")
        
    else:
        ref = db.reference('/' +working_values["name"]+ "/preferences/" +working_values["prev"]+ "_time")
        
    task_time = ref.get()
    print(task_time)
    ser.write((str(task_time)+",").encode("utf-8"))
    return(task_time)

def validation(task_time):
    while True:
        rec = ser.readline().decode('utf-8').strip()
        if (rec != ""):
            if(len(rec) == 4 or len(rec) == 3) and (rec[-1] == "0" or rec[-1] == "1") and (rec[1] == "," or  rec[2] == ","):
                received_values = rec.split(",")
                ser.write((str(2)+",").encode("utf-8"))
                break
            else:
                ser.write((str(1)+",").encode("utf-8"))
    print(received_values)
    return received_values

def update(working_values,date,task_time):
    rec = validation()
    date = datetime.today().date().isoformat()
    print(task_time)
    
    ref = db.reference("/user/days/"+date+"/remaining_times/"+working_values["prev"]+ "_time")
    time = ref.get() - (task_time - int(rec[0]))
    print(time)
    ref = db.reference("/user/days/"+date+"/remaining_times/")
    ref.child(working_values["prev"] + "_time").set(time)


def main():
    date = datetime.today().date().isoformat()
    remaining = rtime()
    print(remaining)
    
    rest_time = today_times(remaining,date)
    print(rest_time)
    
    working_values = start()
    task_time = send(working_values)
    update(working_values,date,task_time)
main()

# def end()


# ser.write("120,".encode("utf-8"))










