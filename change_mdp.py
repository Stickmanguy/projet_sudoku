from send_mail import send_mail_oubli
from hashage import *
import json
import getpass


def change_mdp():

    # Lecture du fichier .json
    with open('user.json', 'r+', encoding='utf-8') as json_file:
        user = input("Username :")
        mail = input('Mail :')
        user_list = json.load(json_file)
        for p in user_list['people']:
            if p['name'] == user and p['mail'] == mail:
                passwd = send_mail_oubli(user, mail)  # Assignation du mdp + envoie du mail
                tmp = p['password']
                print(passwd)
                p['password'] = hash_password(passwd)
                
        json_file.seek(0)  # rewind
        json.dump(user_list, json_file, indent=4)
        json_file.truncate()
        json_file.close()