from hashage import *
import json


def ajout_utilisateur(user, passwd):
    passwd = hash_password(passwd)

    # Lecture du fichier .json
    with open('../user.json', 'r', encoding='utf-8') as json_file:
        user_list = json.load(json_file)
        json_file.close()

    # Assignation du fichier dans une variable type dictionnaire
    data = user_list
    # Ajout d'un utilisateur et d'un mot de passe
    data["people"].append({
        'name': user,
        'password': passwd
    })
    # Ecritue sur le fichier .json
    with open('../user.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
