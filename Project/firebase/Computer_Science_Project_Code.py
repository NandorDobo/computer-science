import matplotlib.pyplot as plt
import numpy as np
import firebase_admin
from firebase_admin import db
import datetime
from datetime import datetime
import serial
from serial.tools.list_ports import comports

PID_MICROBIT = 516
VID_MICROBIT = 3368
TIMEOUT = 0.1
CREDENTIALS_PATH = "C:/Users/22NDobo.ACC/Downloads/project-efc51-firebase-adminsdk-zp4rw-d8b40054e4.json"
 
 
 
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
    
cred = firebase_admin.credentials.Certificate(CREDENTIALS_PATH)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://project-efc51-default-rtdb.europe-west1.firebasedatabase.app'
})



def rtime():
    now = datetime.now()
    hour = now.hour
    minutes = now.minute
    remaining = (22-hour)*60-minutes
    return remaining


def today_times(remaining,date, working_values):
    study_time = int(get_data(f"/{working_values['name']}/times/study_time"))
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
                
    sport_preference = input("How much sport do you do in one session(minutes)")
    ref = db.reference("/" +working_values["name"]+ "/preferences")
    ref.child("sport_time").set(sport_preference)
                
    study_preference = input("How much study do you do in one session(minutes)")
    ref = db.reference("/" +working_values["name"]+ "/preferences")
    ref.child("study_time").set(study_preference)                
                
    rest_preference = input("How much rest do you do after an activity(minutes)")
    ref = db.reference("/" +working_values["name"]+ "/preferences")
    ref.child("rest_time").set(rest_preference)
                
    ref = db.reference("/" +working_values["name"]+ "/times")
    ref.child("study_time").set(40)
    ref.child("sport_time").set(40)
    
    ref = db.reference("/" +working_values["name"]+ "/succes_avarage/")
    ref.child("study").set(0)
    ref.child("study_avarage").set(0)
    ref.child("sport").set(0)
    ref.child("sport_avarage").set(0)
    ref.child("rest").set(0)
    ref.child("rest_avarage").set(0)
    
    weekday = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    for x in weekday:
        ref = db.reference("/" +working_values["name"]+ "/times_avarage/"+x)
        ref.child("study").set(0)
        ref.child("study_avarage").set(0)
        ref.child("sport").set(0)
        ref.child("sport_avarage").set(0)
    
def start(date):
    working_values = {}
    working_values["previous_activity"] = ""
    while True:
        new_or_not = input("Are you a new user?")
        if (new_or_not.lower() in ["yes", 'y']):
            working_values["name"] = input("What is your name?")
            ref = db.reference("/" +working_values["name"])
            if ref.get():
                print("The name already exist chose a new one or log into that one")
            else:
                setup(working_values)
                break
            
        elif(new_or_not.lower() in ["no","n"]):
            working_values["name"] = input("What is your name?")
            ref = db.reference("/" +working_values["name"])
            if ref.get():
                break
            else:
                print("The name does not exists, try again if you misspelled or if you dont have an account create one")
                
    weekday_value = weekday(date,working_values)
    print(weekday_value)
    if(input("Do you want to see your data graphed?") == "yes"):    
        graph(working_values,date,weekday_value)
    
    if(input("Do you want to see predictions for your day?") == "yes"):
        what_if(working_values,date,weekday_value)
    while(working_values["previous_activity"] != "sport" and working_values["previous_activity"] != "study" and working_values["previous_activity"] != "rest"):
        print("What do you want to do first?")
        working_values["previous_activity"] = input("(study,sport,rest)")
    
    ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/")
    ref.child("start").set(working_values["previous_activity"])
    
    return working_values

def graph(working_values,date,weekday_value):
    if(input("Do you want to see the graph of your avarage success?") == "yes"):
        avarage_success_graph(working_values,date,weekday_value)
    if(input("Do you want to see the graph of your avarage times?") == "yes"):
        avarage_times_graph(working_values,date,weekday_value)
    if(input("Do you want to see the graph of your past success?") == "yes"):
        past_success_graph(working_values,date,weekday_value)

def avarage_success_graph(working_values,date,weekday_value):
    fig, ax = plt.subplots()

    ref = db.reference("/" +working_values["name"]+ "/success_avarage/study_avarage")
    study_avarage = ref.get()
    
    ref = db.reference("/" +working_values["name"]+ "/success_avarage/sport_avarage")
    sport_avarage = ref.get()
    
    ref = db.reference("/" +working_values["name"]+ "/success_avarage/rest_avarage")
    rest_avarage = ref.get()



    starting = ['study', 'sport', 'rest']
    counts = [study_avarage,sport_avarage,rest_avarage]
    bar_labels = ["success","success","success"]
    bar_colors = ['tab:red', 'tab:blue', 'tab:red']

    ax.bar(starting, counts, color=bar_colors)

    ax.set_ylabel('Avarage success per day')
    ax.set_title('Avarage success by starting activity')

    plt.show()

def avarage_times_graph(working_values,date,weekday_value):
    weekday = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    avarage = {}

    for x in weekday:
        avarage[x + "sport"] = get_data(f"/{working_values['name']}/times_avarage/{x}/sport")
        avarage[x + "study"] = get_data(f"/{working_values['name']}/times_avarage/{x}/study")

    species = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
    sport_times = np.array([
        avarage["mondaysport"],
        avarage["tuesdaysport"],
        avarage["wednesdaysport"],
        avarage["thursdaysport"],
        avarage["fridaysport"],
        avarage["saturdaysport"],
        avarage["sundaysport"]
    ])

    study_times = np.array([
        avarage["mondaystudy"],
        avarage["tuesdaystudy"],
        avarage["wednesdaystudy"],
        avarage["thursdaystudy"],
        avarage["fridaystudy"],
        avarage["saturdaystudy"],
        avarage["sundaystudy"]
    ])

    width = 0.35
    x = np.arange(len(species))

    fig, ax = plt.subplots()

    p1 = ax.bar(x, sport_times, width, label='Sport')
    p2 = ax.bar(x, study_times, width, bottom=sport_times, label='Study')

    ax.set_xlabel('Days of the week')
    ax.set_ylabel('Average time')
    ax.set_title('Average Time Spent on Sport and Study per Day')
    ax.set_xticks(x)
    ax.set_xticklabels(species)
    ax.legend()

    plt.show()

def past_success_graph(working_values,date,weekday_value):
    
    ref = db.reference(f"/{working_values['name']}/days")
    data_key = "success"
    name_data_list = get_past_data(ref, data_key)

    folder_names = list(name_data_list.keys())
    data = [folder_data for folder_data in name_data_list.values()]
    
    
    plt.bar(folder_names, data)
    plt.xlabel('Days')
    plt.ylabel('success')
    plt.title('success per day')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    

def get_past_data(ref, data_key):
    name_data_list = {}
    children = ref.get()
    if children:
        for key, value in children.items():
            if isinstance(value, dict):
                name_data_list[key] = value.get(data_key)
    return name_data_list
    

def get_data(path):
    return db.reference(path).get()
    
def what_if(working_values,date,weekday):
    if(input("Do you want to see what your predicted success is based on your previous data, if you start with a specific activity? ") == "yes"):
        activity = input("For wich activity would you like to see the prediction?(sport,study,rest)")
        
        print("Your predicted avarage success for today starting with " +activity+ " Is: " + str(get_data(f"/{working_values['name']}/success_avarage/{activity}_avarage")))
        
        
    if(input("Do you want to see what if you did more of a specific activity, whether it would improve or not your health") == "yes"):
        
        activity = input("For wich activity would you like to see the prediction?(sport,study)")
        avarage = get_data(f"/{working_values['name']}/times_avarage/{weekday}/{activity}_avarage")
        ideal = get_data(f"/{working_values['name']}/times/{activity}_time")
        if avarage < ideal:
            print(f"Yes, the model indicates that doing more {activity} would improve your health")
        else:
            print("You dont need to do more of that, you should be able have a balanced life if you do the usual amount ")
    if(input("Do you want to check other things") == "yes"):
        what_if(working_values,date,weekday)
    
def send(working_values,date):
    if(working_values["previous_activity"] == "rest" and get_data(f"/{working_values['name']}/days/{date}/remaining_times/sport_time") == 0 and get_data(f"/{working_values['name']}/days/{date}/remaining_times/sport_time") == 0):
        task_time = get_data(f"/{working_values['name']}/days/{date}/remaining_times/rest_time")
    else:
        task_time = get_data(f"/{working_values['name']}/preferences/{working_values['previous_activity']}_time")
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
    return received_values

def update(working_values,date,task_time):
    rec = validation()
    
    ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/remaining_times/"+working_values["previous_activity"]+ "_time")
    time = int(ref.get()) - (int(task_time) - int(rec[0]))
    
    ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/remaining_times/")
    ref.child(working_values["previous_activity"] + "_time").set(time)
    if(working_values["previous_activity"] != "rest"):
        ref = db.reference("/" +working_values["name"]+"/days/"+date+"/success/")
        success = ref.get()
        ref = db.reference("/" +working_values["name"]+"/days/"+date+"/")
        ref.child("success").set(success + int(rec[-1]))
    
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
        
    ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/")
    ref.child("day_of_week").set(day_of_week)
    return day_of_week
    
def success_avarage(working_values,date):
    ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/success")
    success = ref.get()
    
    ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/start")
    start  = ref.get()
    
    ref = db.reference("/" +working_values["name"]+ "/success_avarage/"+start)
    times = ref.get()
    ref = db.reference("/" +working_values["name"]+ "/success_avarage/" +start+ "_avarage")
    avarage = ref.get()
    
    new_avarage = ((avarage*times)+success)/(times+1)
    ref = db.reference("/" +working_values["name"]+ "/success_avarage")
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
    get_data = lambda path : db.reference(path).get()
    
    
    sport = get_data(f"/{working_values['name']}/times_avarage/{weekday}/sport")
    sport_avarage = get_data(f"/{working_values['name']}/times_avarage/{weekday}/sport_avarage")
    
    study = get_data(f"/{working_values['name']}/times_avarage/{weekday}/study")
    study_avarage = get_data(f"/{working_values['name']}/times_avarage/{weekday}/study_avarage")
    

    new_avarage = ((sport_avarage*sport)+times_done["sport"])/(sport+1)
    ref = db.reference(f"/{working_values['name']}/times_avarage/{weekday}")
    ref.child("sport").set(sport+1)
    ref.child("sport_avarage").set(new_avarage)

    
    new_avarage = ((study_avarage*study)+times_done["study"])/(study+1)
    ref = db.reference(f"/{working_values['name']}/times_avarage/{weekday}")
    ref.child("study").set(study+1)
    ref.child("study_avarage").set(new_avarage)
    

def main():
    date = datetime.today().date().isoformat()
    print(date)
    working_values = start(date)
    
    
    remaining = rtime()
    
    ref = db.reference("/" +working_values["name"]+ "/days/"+date+"/")
    ref.child("success").set(0)
    
    weekday_value = weekday(date,working_values)
    
    today_times(remaining,date,working_values)
    
    task_time = int(send(working_values,date))
    update(working_values,date,task_time)
    while True:
        if(remaining < 30):
            print("It is time to go to bed get ready for it. Good Night")
            break
        recommended = recommend(working_values,date)
        while(working_values["previous_activity"] != "sport" and working_values["previous_activity"] != "study" and working_values["previous_activity"] != "rest"):
            working_values["previous_activity"] = str(input("What do you want to do next?, I recommend "+recommended))

        if(working_values["previous_activity"] == "end"):
            break

        task_time = send(working_values,date)
        update(working_values,date,task_time)


    
    success_avarage(working_values,date)
    
    times_done = done_time(working_values,date)
    done_time_avarage(times_done,working_values,date,weekday_value)


if __name__ == '__main__':
    main()








