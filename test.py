import smtplib
import random
import string


random_mdp = random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + str(random.randint(1, 500)) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
rec_email = "fleondespam@gmail.com"
sender_email = "sudoku.mania.mod@gmail.com"
password = "Az@rty123456"
message = "Voici votre nouveau mot de passe" + str(random_mdp) + " (changez le vite)"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print('login success')
server.sendmail(sender_email, rec_email, message)
print("mail has been send")
