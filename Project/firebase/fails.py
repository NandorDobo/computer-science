import matplotlib.pyplot as plt
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("C:/Users/22NDobo.ACC/info/Project/firebase/project-efc51-firebase-adminsdk-zp4rw-d8b40054e4.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://project-efc51-default-rtdb.europe-west1.firebasedatabase.app'
})

working_values = {}
working_values["name"] = input("What is your name")

fig, ax = plt.subplots()

ref = db.reference("/" +working_values["name"]+ "/fails_avarage/study_avarage")
study_avarage = ref.get()
    
ref = db.reference("/" +working_values["name"]+ "/fails_avarage/sport_avarage")
sport_avarage = ref.get()
    
ref = db.reference("/" +working_values["name"]+ "/fails_avarage/rest_avarage")
rest_avarage = ref.get()



starting = ['study', 'sport', 'rest']
counts = [study_avarage,sport_avarage,rest_avarage]
bar_labels = ["fails","fails","fails"]
bar_colors = ['tab:red', 'tab:blue', 'tab:red']

ax.bar(starting, counts, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
# ax.legend(title='Fruit color')

plt.show()