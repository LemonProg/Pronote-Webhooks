import pronotepy
from pronotepy.ent import ent_var
from datetime import datetime
from datetime import timedelta
import datetime as dt
import requests

date = datetime.date(datetime.now()) # Date today
date2 = date + timedelta(days=3) # Current date + 4 days (for testing)

timetable = "put your discord webhook"

data = {
    "username": "Emploie du temps",
    "embeds": [{
        "title": f"Journée du {date}"
    }]
}

x = requests.post(timetable, json=data)

client = pronotepy.Client('put your direct link pronote url',
                   username='...',
                   password='...',
                   ent=...)

if client.logged_in:
    lessons = client.lessons(date)
    
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
    
    menus = client.menus(date
                        )
    
    for menu in menus:
        cantine = {
            "username": "Cuisinier",
            "avatar_url": "https://i.pinimg.com/originals/dd/9d/c9/dd9dc9d83423bc037b511d73b29e6b80.png",
            "embeds": [{
                'title': f'Repas du {menu.date}',
            }]
        }
        z = requests.post(timetable, json=cantine)
        
        for first_meal in menu.first_meal:
            cantine = {
                "username": "Cuisinier",
                "avatar_url": "https://i.pinimg.com/originals/dd/9d/c9/dd9dc9d83423bc037b511d73b29e6b80.png",
                "embeds": [{
                    'description': f'Entrée - {first_meal.name}',
                }]
            }
            z = requests.post(timetable, json=cantine)
            
        for main_meal in menu.main_meal:
            cantine = {
                "username": "Cuisinier",
                "avatar_url": "https://i.pinimg.com/originals/dd/9d/c9/dd9dc9d83423bc037b511d73b29e6b80.png",
                "embeds": [{
                    'description': f'Plat Principal - {main_meal.name}',
                }]
            }
            z = requests.post(timetable, json=cantine)
                
        try:
            for side_meal in menu.side_meal:
                cantine = {
                    "username": "Cuisinier",
                    "avatar_url": "https://i.pinimg.com/originals/dd/9d/c9/dd9dc9d83423bc037b511d73b29e6b80.png",
                    "embeds": [{
                        'description': f'Second Plat - {side_meal.name}',
                    }]
                }
                z = requests.post(timetable, json=cantine)
        except TypeError:
            pass
                
        for cheese in menu.cheese:
            cantine = {
                "username": "Cuisinier",
                "avatar_url": "https://i.pinimg.com/originals/dd/9d/c9/dd9dc9d83423bc037b511d73b29e6b80.png",
                "embeds": [{
                    'description': f'Dessert/Fromage - {cheese.name}',
                }]
            }
            z = requests.post(timetable, json=cantine)
                    
        for desert in menu.dessert:
            cantine = {
                "username": "Cuisinier",
                "avatar_url": "https://i.pinimg.com/originals/dd/9d/c9/dd9dc9d83423bc037b511d73b29e6b80.png",
                "embeds": [{
                    'description': f'Dessert/Fromage - {desert.name}',
                }]
            }
            z = requests.post(timetable, json=cantine)
    
    datas = {
        "username": "Emploie du temps",
        "embeds": [{
            "title": f"Bonne journée *{client.info.name}*"
        }]
    }
    
    y = requests.post(timetable, json=datas)       
else:
    print('no login')

