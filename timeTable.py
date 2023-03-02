import pronotepy
# from pronotepy.ent import YOUR ENT
from datetime import datetime
from datetime import timedelta
import datetime as dt
import requests

date = datetime.date(datetime.now()) # Date today
date2 = date + timedelta(days=3) # Date in 5 days

timetable = "enter ur webbook"

data = {
    "username": "Emploie du temps",
    "embeds": [{
        "title": f"Journée du {date2}"
    }]
}

x = requests.post(timetable, json=data)

client = pronotepy.Client('direct link to pronote !',
                   username='user',
                   password='password',
                   ent="enter ur ent")

if client.logged_in:
    lessons = client.lessons(date2)
    
    for lesson in lessons:
        color = int(lesson.background_color.replace('#', ''), base=16)
        hourStart = lesson.start.strftime('%H:%M')
        hourEnd = lesson.end.strftime('%H:%M')
        
        datas = {
            "username": "Emploie du temps",
            "embeds": [{
                "title": f"Matière : {lesson.subject.name}",
                "description": f"Prof : {lesson.teacher_name} \nHoraires : {hourStart} / {hourEnd}",
                "color": color
            }],
        }
        if lesson.canceled:
            datas = {}

        y = requests.post(timetable, json=datas)
    
    datas = {
        "username": "Emploie du temps",
        "embeds": [{
            "title": f"Bonne journée *{client.info.name}*"
        }]
    }
    
    y = requests.post(timetable, json=datas)       
else:
    print('no login')

