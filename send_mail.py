from verif_utilisateur import verif_mail
import json
import smtplib
import string
import random

random_mdp = random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + str(random.randint(1, 500)) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)


def send_mail_bienvenue(username):
    rec_email = verif_mail(username)
    sender_email = "sudoku.mania.mod@gmail.com"
    password = "Az@rty123456"

    message = "Bienvenue sur sudoku mania, merci pour votre inscription, " + str(username) + ", Bon amusement"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    print('login success')
    server.sendmail(sender_email, rec_email, message)
    print("mail has been send")


def send_mail_oubli(username, rec_email):
    if rec_email == verif_mail(username):
        sender_email = "sudoku.mania.mod@gmail.com"
        password = "Az@rty123456"
        message = "Voici votre nouveau mot de passe " + str(random_mdp) + " (changez le vite)"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print('login success')
        server.sendmail(sender_email, rec_email, message)
        print("mail has been send")
        return str(random_mdp)