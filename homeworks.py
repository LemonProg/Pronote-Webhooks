import pronotepy
# from pronotepy.ent import YOUR ENT
from datetime import datetime
from datetime import timedelta
import requests

date = datetime.date(datetime.now()) # Date today
date2 = date + timedelta(days=2) # Date in 2 days

devoirs = "enter ur webbook"

client = pronotepy.Client('direct link to pronote !',
                   username='user',
                   password='password',
                   ent="enter ur ent")


if client.logged_in:
    homeworks = client.homework(date, date2)
    
    datas = {
        "username": "Devoirs",
        "embeds": [{
            "title": f"Bonjour *{client.info.name}*",
            "description": f"Vous avez **{len(homeworks)}** devoir(s)",
        }],
    }
    x = requests.post(devoirs, json=datas)
    
    for work in homeworks:
        def setDatas(description, color):
            datas = {
                "username": "Devoirs",
                "embeds": [{
                    "title": f"Matière : {work.subject.name}",
                    "description": description,
                    "color": color
                }],
            }

            y = requests.post(devoirs, json=datas)
        
        if work.done == True:
            couleur = "65280"
            
            timeLeft = work.date - date
            timeLeft = str(timeLeft)[:2]
            
            desc = f"{work.description} \n\n Pour le {work.date} ({timeLeft} jours) \n État : Fait"
            setDatas(desc, couleur)
        else:
            timeLeft = work.date - date
            timeLeft = str(timeLeft)[:2]
          
            couleur = "16711680"
            desc = f"{work.description} \n\n Pour le {work.date} ({timeLeft} jours) \n État : Non Fait"
            setDatas(desc, couleur)
        
        for file in work.files:
            datas = {
                "username": "Devoirs",
                "embeds": [{
                    "description": f"[{file.name}]({file.url})",
                }],
            }
            y = requests.post(devoirs, json=datas)        
else:
    print('no login')
