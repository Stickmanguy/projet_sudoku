from hashage import *
from send_mail import *
import json
import getpass


def ajout_utilisateur():
    user = input("Username :")
    mail = input('Mail :')
    passwd = getpass.getpass("Votre mot de passe :")
    passwd = hash_password(passwd)

    # Lecture du fichier .json
    with open('user.json', 'r', encoding='utf-8') as json_file:
        user_list = json.load(json_file)
        json_file.close()

    # Assignation du fichier dans une variable type dictionnaire
    data = user_list
    # Ajout d'un utilisateur et d'un mot de passe
    data["people"].append({
        'name': user,
        'password': passwd,
        'mail': mail,
        'classement': 500
    })
    # Ecritue sur le fichier .json
    with open('user.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
    send_mail_bienvenue(user)