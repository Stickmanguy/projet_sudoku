from send_mail import send_mail_oubli
from hashage import *
import json


def mdp_oubli(user, mail):
    # Lecture du fichier .json
    with open('user.json', 'r+', encoding='utf-8') as json_file:
        user_list = json.load(json_file)
        for p in user_list['people']:
            if p['name'] == user and p['mail'] == mail:
                passwd = send_mail_oubli(user, mail)  # Assignation du mdp + envoie du mail
                p['password'] = hash_password(passwd)

        json_file.seek(0)  # rewind
        json.dump(user_list, json_file, indent=4)
        json_file.truncate()
        json_file.close()


def change_mdp(old_pass, new_pass, user):
    with open('user.json', 'r+', encoding='utf-8') as json_file:
        user_list = json.load(json_file)
        for p in user_list['people']:
            if p['name'] == user and verify_password(p['password'], old_pass):
                print(old_pass)
                print(new_pass)
                p['password'] = hash_password(new_pass)

        json_file.seek(0)  # rewind
        json.dump(user_list, json_file, indent=4)
        json_file.truncate()
        json_file.close()
