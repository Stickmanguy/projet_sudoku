from hashage import *
import json


def verif_utilisateur(username, passwd):
    with open('user.json', 'r', encoding='utf-8') as json_file:
        user_list = json.load(json_file)
        json_file.close()
        for p in user_list['people']:
            if p['name'] == username:
                return verify_password(p['password'], passwd)


def verif_mail(username):
    with open('user.json', 'r', encoding='utf-8') as json_file:
        user_list = json.load(json_file)
        json_file.close()
        for p in user_list['people']:
            if p['name'] == username:
                return p['mail']
