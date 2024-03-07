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
    print('microbit not found, connect microbit to the computer and restart the program')
    exit()
else:    
    ser.open()
    
cred = credentials.Certificate("C:/Users/22NDobo.ACC/info/Project/firebase/project-efc51-firebase-adminsdk-zp4rw-d8b40054e4.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://project-efc51-default-rtdb.europe-west1.firebasedatabase.app'
})



#Read
# ref = db.reference('/" +working_values["name"]+ "/resttime')
# snapshot = ref.get()
# print(snapshot)


def rtime():
    now = datetime.now()
    hour = now.hour
    minutes = now.minute
    remaining = (22-hour)*60-minutes
    return remaining


def today_times(remaining,date, working_values):
    ref = db.reference("/" +working_values["name"]+ "/times/study_time")
    study_time = int(ref.get())
    remaining -= study_time
    ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/remaining_times")
    ref.child("study_time").set(study_time)
    
    
    ref = db.reference("/" +working_values["name"]+ "/times/sport_time")
    sport_time = int(ref.get())
    remaining -= sport_time
    ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/remaining_times")
    ref.child("sport_time").set(sport_time)
    
    ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/remaining_times")
    ref.child("rest_time").set(remaining)

    
def setup(working_values):
    ref = db.reference("/"+working_values["name"])
                
    sport_preference = input("How much sport do you do in one session")
    ref = db.reference("/" +working_values["name"]+ "/preferences")
    ref.child("sport_time").set(sport_preference)
                
    study_preference = input("How much study do you do in one session")
    ref = db.reference("/" +working_values["name"]+ "/preferences")
    ref.child("study_time").set(study_preference)                
                
    rest_preference = input("How much rest do you do after an activity")
    ref = db.reference("/" +working_values["name"]+ "/preferences")
    ref.child("rest_time").set(rest_preference)
                
    ref = db.reference("/" +working_values["name"]+ "/times")
    ref.child("study_time").set(40)
    ref.child("sport_time").set(40)
    
    ref = db.reference("/" +working_values["name"]+ "/fails_avarage/")
    ref.child("study").set(0)
    ref.child("study_avarage").set(0)
    ref.child("sport").set(0)
    ref.child("sport_avarage").set(0)
    ref.child("rest").set(0)
    ref.child("rest_avarage").set(0)
    
    ref = db.reference("/" +working_values["name"]+ "/times_avarage/monday")
    ref.child("study").set(0)
    ref.child("study_avarage").set(0)
    ref.child("sport").set(0)
    ref.child("sport_avarage").set(0)
    
    ref = db.reference("/" +working_values["name"]+ "/times_avarage/tuesday")
    ref.child("study").set(0)
    ref.child("study_avarage").set(0)
    ref.child("sport").set(0)
    ref.child("sport_avarage").set(0)
    
    ref = db.reference("/" +working_values["name"]+ "/times_avarage/wednesday")
    ref.child("study").set(0)
    ref.child("study_avarage").set(0)
    ref.child("sport").set(0)
    ref.child("sport_avarage").set(0)
    
    ref = db.reference("/" +working_values["name"]+ "/times_avarage/thursday")
    ref.child("study").set(0)
    ref.child("study_avarage").set(0)
    ref.child("sport").set(0)
    ref.child("sport_avarage").set(0)
    
    ref = db.reference("/" +working_values["name"]+ "/times_avarage/friday")
    ref.child("study").set(0)
    ref.child("study_avarage").set(0)
    ref.child("sport").set(0)
    ref.child("sport_avarage").set(0)
    
    ref = db.reference("/" +working_values["name"]+ "/times_avarage/saturday")
    ref.child("study").set(0)
    ref.child("study_avarage").set(0)
    ref.child("sport").set(0)
    ref.child("sport_avarage").set(0)
    
    ref = db.reference("/" +working_values["name"]+ "/times_avarage/sunday")
    ref.child("study").set(0)
    ref.child("study_avarage").set(0)
    ref.child("sport").set(0)
    ref.child("sport_avarage").set(0)


def start(date):
    working_values = {}
    while True:
        new_or_not = input("Are you a new user?")
        if (new_or_not == "yes"):
            working_values["name"] = input("What is your name?")
            ref = db.reference("/" +working_values["name"])
            if ref.get():
                print("The name already exist chose a new one or log into that one")
            else:
                setup(working_values)
                break
            
        elif(new_or_not == "no"):
            working_values["name"] = input("What is your name?")
            ref = db.reference("/" +working_values["name"])
            if ref.get():
                break
            else:
                print("The name does not exists, try again if you misspelled or if you dont have an account create one")
    print("What do you want to do first?")
    previous_activity = input("study,sport,rest")
    
    ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/")
    ref.child("start").set(previous_activity)
    
    working_values["previous_activity"] = previous_activity
    return working_values


def send(working_values):
    ref = db.reference('/' +working_values["name"]+ "/preferences/" +working_values["previous_activity"]+ "_time") 
    task_time = ref.get()
    
    print(task_time)
    ser.write((str(task_time)+",").encode("utf-8"))
    return(task_time)

def validation():
    while True:
        rec = ser.readline().decode('utf-8').strip()
        if (rec != ""):
            if(rec[-1] == "0" or rec[-1] == "1") and (rec[1] == "," or  rec[2] == ",") and (rec[-2] == ","):
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
    
    ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/remaining_times/"+working_values["previous_activity"]+ "_time")
    time = int(ref.get()) - (int(task_time) - int(rec[0]))
    
    print(time)
    ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/remaining_times/")
    ref.child(working_values["previous_activity"] + "_time").set(time)
    if(working_values["previous_activity"] != "rest"):
        ref = db.reference("/" +working_values["name"]+"/days/"+date+"/fails/")
        fail = ref.get()
        ref = db.reference("/" +working_values["name"]+"/days/"+date+"/")
        ref.child("fails").set(fail + int(rec[-1]))
    
def recommend(working_values,date):
    if(working_values["previous_activity"] == "sport"):
        recommend = "rest"
    elif(working_values["previous_activity"] == "study"):
        ref = db.reference("/" +working_values["name"]+"/days/"+date+"/remaining_times/"+"sport_time")
        if(ref.get() != 0):
            recommend = "sport"
        else:
            recommend = "rest"
    else:
        ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/remaining_times/"+"study_time")
        study_time = ref.get()
        ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/remaining_times/"+"sport_time")
        sport_time = ref.get()
        if(study_time != 0):
            recommend = "study"
        elif(sport_time != 0):
            recommend = "sport"
        else:
            recommend = "rest"
    return recommend

def weekday(date,working_values):
    date_parts = date.split("-")
    year = int(date_parts[0])
    month = int(date_parts[1])
    day = int(date_parts[2])
    given_date = datetime(year, month, day)
    day_of_week = given_date.weekday()

    day_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"][day_of_week]
    print(day_of_week)
        
    ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/")
    ref.child("day_of_week").set(day_of_week)
    
def fails_avarage(working_values,date):
    ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/fails")
    fails = ref.get()
    
    ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/start")
    start  = ref.get()
    
    ref = db.reference("/" +working_values["name"]+ "/fails_avarage/"+start)
    times = ref.get()
    ref = db.reference("/" +working_values["name"]+ "/fails_avarage/" +start+ "_avarage")
    avarage = ref.get()
    
    new_avarage = ((avarage*times)+fails)/(times+1)
    ref = db.reference("/" +working_values["name"]+ "/fails_avarage")
    ref.child(start).set(times+1)
    ref.child(start + "_avarage").set(new_avarage)
    
def done_time(working_values,date):
    times_done = {}
    ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/remaining_times/"+"sport_time")
    sport = ref.get()
    ref = db.reference("/" +working_values["name"]+ "/times/sport_time")
    sport_all = ref.get()
    times_done["sport"] = sport_all - sport
    
    
    ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/remaining_times/"+"study_time")
    study = ref.get()
    ref = db.reference("/" +working_values["name"]+ "/times/study_time")
    study_all = ref.get()
    times_done["study"] = study_all - study
    
    return times_done
    


def done_time_avarage(times_done, working_values,date,weekday):
    get_path = lambda path : db.reference(path).get()
    sport = get_path(f"/{working_values['name']}/times_avarage/{weekday}/sport")
    sport_avarage = get_path(f"/{working_values['name']}/times_avarage/{weekday}/sport_avarage")
    
    ref = db.reference("/" +working_values["name"]+ "/times_avarage/"+weekday+"/study")
    study = ref.get()
    ref = db.reference("/" +working_values["name"]+ "/times_avarage/"+weekday+"/study_avarage")
    study_avarage = ref.get()
    
    new_avarage = ((sport_avarage*sport)+times_done["sport"])/(sport+1)
    ref = db.reference("/" +working_values["name"]+ "/fails_avarage")
    ref.child(sport).set(sport+1)
    ref.child("sport_avarage").set(new_avarage)

    
    new_avarage = ((avarage*times)+fails)/(times+1)
    ref = db.reference("/" +working_values["name"]+ "/fails_avarage")
    ref.child(start).set(times+1)
    ref.child(start + "_avarage").set(new_avarage)
    
def end(working_values,date,weekday):
    fails_avarage(working_values,date)
    
    times_done = done_time(working_values,date)
    done_time_avarage(times_done,working_values,date,weekday)
#     
    
def main():
    date = datetime.today().date().isoformat()
    working_values = start(date)
    
    remaining = rtime()
    print(remaining)
    
    ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/")
    ref.child("fails").set(0)
    
    weekday1 = weekday(date,working_values)
    
    rest_time = today_times(remaining,date,working_values)
    print(rest_time)
    
    task_time = int(send(working_values))
    update(working_values,date,task_time)
    while True:
        recommended = recommend(working_values,date)
        print("What do you want to do next?, I recommend "+recommended)
        previous_activity = input()
        if(previous_activity == "end"):
            break
        working_values["previous_activity"] = str(previous_activity)
        task_time = send(working_values)
        update(working_values,date,task_time)

        if(remaining == 30):
            print("It is time to go to bed get ready for it. Good Night")
            break
    
    end(working_values,date,weekday)
main()

# def end()


# ser.write("120,".encode("utf-8"))










