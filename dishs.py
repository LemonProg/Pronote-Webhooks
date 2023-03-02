import pronotepy
# from pronotepy.ent import YOUR ENT
from datetime import datetime
from datetime import timedelta
import datetime as dt
import requests

date = datetime.date(datetime.now()) # Date today

repas = "enter ur webbook"

client = pronotepy.Client('direct link to pronote !',
                   username='user',
                   password='password',
                   ent="enter ur ent")

if client.logged_in:
    menus = client.menus(date)
    
    for menu in menus:
        cantine = {
            "username": "Cuisinier",
            "avatar_url": "https://i.pinimg.com/originals/dd/9d/c9/dd9dc9d83423bc037b511d73b29e6b80.png",
            "embeds": [{
                'title': f'Repas du {menu.date}',
            }]
        }
        z = requests.post(repas, json=cantine)
        
        for first_meal in menu.first_meal:
            cantine = {
                "username": "Cuisinier",
                "avatar_url": "https://i.pinimg.com/originals/dd/9d/c9/dd9dc9d83423bc037b511d73b29e6b80.png",
                "embeds": [{
                    'description': f'Entrée - {first_meal.name}',
                }]
            }
            z = requests.post(repas, json=cantine)
            
        for main_meal in menu.main_meal:
            cantine = {
                "username": "Cuisinier",
                "avatar_url": "https://i.pinimg.com/originals/dd/9d/c9/dd9dc9d83423bc037b511d73b29e6b80.png",
                "embeds": [{
                    'description': f'Plat Principal - {main_meal.name}',
                }]
            }
            z = requests.post(repas, json=cantine)
                
        try:
            for side_meal in menu.side_meal:
                cantine = {
                    "username": "Cuisinier",
                    "avatar_url": "https://i.pinimg.com/originals/dd/9d/c9/dd9dc9d83423bc037b511d73b29e6b80.png",
                    "embeds": [{
                        'description': f'Second Plat - {side_meal.name}',
                    }]
                }
                z = requests.post(repas, json=cantine)
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
            z = requests.post(repas, json=cantine)
                    
        for desert in menu.dessert:
            cantine = {
                "username": "Cuisinier",
                "avatar_url": "https://i.pinimg.com/originals/dd/9d/c9/dd9dc9d83423bc037b511d73b29e6b80.png",
                "embeds": [{
                    'description': f'Dessert/Fromage - {desert.name}',
                }]
            }
            z = requests.post(repas, json=cantine)
    
    datas = {
        "username": "Cuisinier",
        "embeds": [{
            "title": f"Bonne appétit *{client.info.name}*"
        }]
    }
    
    y = requests.post(repas, json=datas)       
else:
    print('no login')

