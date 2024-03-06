import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime
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
    
cred = credentials.Certificate("C:/Users/Nandi/Downloads/project-efc51-firebase-adminsdk-zp4rw-d8b40054e4.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://project-efc51-default-rtdb.europe-west1.firebasedatabase.app'
})

ref = db.reference("/user")
ref.child("small_rest_preference").set(10)
ref = db.reference("/user/preferences")
ref.child("study_time").set(20)
ref.child("sport_time").set(20)
ref = db.reference("/user/times")
ref.child("study_time").set(0)
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
    
    ref = db.reference("/user/days/"+date+"/remaining_times")
    ref.child("rest_time").set(remaining)

    

def start(date):
    name = input("What is your username?")
    print("What do you want to do first?")
    previous_activity = input("study,sport,rest")
    working_values = {}
    working_values["name"] = name
    
    ref = db.reference("/user/days/"+date+"/")
    ref.child("start").set(previous_activity)
    
    working_values["previous_activity"] = previous_activity
    return working_values


def send(working_values):
    if(working_values["previous_activity"] == "rest"):
        ref = db.reference('/' +working_values["name"]+ "/small_rest_preference")
        
    else:
        ref = db.reference('/' +working_values["name"]+ "/preferences/" +working_values["previous_activity"]+ "_time")
        
    task_time = ref.get()
    print(task_time)
    ser.write((str(task_time)+",").encode("utf-8"))
    return(task_time)

def validation():
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
    print(task_time)
    
    ref = db.reference("/user/days/"+date+"/remaining_times/"+working_values["previous_activity"]+ "_time")
    time = ref.get() - (task_time - int(rec[0]))
    
    print(time)
    ref = db.reference("/user/days/"+date+"/remaining_times/")
    ref.child(working_values["previous_activity"] + "_time").set(time)
    
    ref = db.reference("/user/days/"+date+"/fails/")
    fail = ref.get()
    ref = db.reference("/user/days/"+date+"/")
    ref.child("fails").set(fail + int(rec[1]))
    
def recommend(working_values,date):
    if(working_values["previous_activity"] == "sport"):
        recommend = "rest"
    elif(working_values["previous_activity"] == "study"):
        ref = db.reference("/user/days/"+date+"/remaining_times/"+"sport_time")
        if(ref.get() != 0):
            recommend = "sport"
        else:
            recommend = "rest"
    else:
        ref = db.reference("/user/days/"+date+"/remaining_times/"+"study_time")
        study_time = ref.get()
        ref = db.reference("/user/days/"+date+"/remaining_times/"+"sport_time")
        sport_time = ref.get()
        if(study_time != 0):
            recommend = "study"
        elif(sport_time != 0):
            recommend = "sport"
        else:
            recommend = "rest"
    return recommend

def weekday(date):
    date_parts = date.split("-")
    year = int(date_parts[0])
    month = int(date_parts[1])
    day = int(date_parts[2])
    given_date = datetime(year, month, day)
    day_of_week = given_date.weekday()

    
    if(day_of_week == 0):
        day_of_week = "monday"
    elif(day_of_week == 1):
        day_of_week = "tuesday"
    elif(day_of_week == 2):
        day_of_week = "wednesday"
    elif(day_of_week == 3):
        day_of_week = "thursday"
    elif(day_of_week == 4):
        day_of_week = "friday"
    elif(day_of_week == 5):
        day_of_week = "saturday"
    else:
        day_of_week = "sunday"
        
    ref = db.reference("/user/days/"+date+"/")
    ref.child("day_of_week").set(day_of_week)

def main():
    date = datetime.today().date().isoformat()
    remaining = rtime()
    print(remaining)
    ref = db.reference("/user/days/"+date+"/")
    ref.child("fails").set(0)
    
    weekday(date)
    
    rest_time = today_times(remaining,date)
    print(rest_time)
    
    working_values = start(date)
    task_time = send(working_values)
    update(working_values,date,task_time)
    while True:
        recommended = recommend(working_values,date)
        print("What do you want to do next?, I recommend "+recommended)    
        previous_activity = input()
        working_values["previous_activity"] = str(previous_activity)
        task_time = send(working_values)
        update(working_values,date,task_time)

        if(remaining == 30):
            print("It is time to go to bed get ready for it. Good Night")
            break
    
main()

# def end()


# ser.write("120,".encode("utf-8"))










