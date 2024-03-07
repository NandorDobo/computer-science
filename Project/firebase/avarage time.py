import matplotlib.pyplot as plt
import numpy as np
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("C:/Users/22NDobo.ACC/info/Project/firebase/project-efc51-firebase-adminsdk-zp4rw-d8b40054e4.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://project-efc51-default-rtdb.europe-west1.firebasedatabase.app'
})

working_values = {}
working_values["name"] = input("What is your name")

get_data = lambda path: db.reference(path).get()
weekday = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
avarage = {}

for x in weekday:
    avarage[x + "sport"] = get_data(f"/{working_values['name']}/times_avarage/{x}/sport")
    avarage[x + "study"] = get_data(f"/{working_values['name']}/times_avarage/{x}/study")

print(avarage)

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
