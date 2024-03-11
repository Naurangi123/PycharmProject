import smtplib
from email.mime.text import MIMEText

body='''This is my text mail.This is sent to you from my python program. I think you appeciated me. Thank You （￣︶￣）↗
Why did the man put his money in the blender?

Because he wanted to make liquid assets!　'''
msg= MIMEText(body)
fromaddr='naurangilal15072002@gmail.com'
toaddr='naurangilal9675329115@gmail.com'

msg['From']=fromaddr
msg['To']=toaddr
msg['Subject']='Hii Buddy'

server=smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login(fromaddr,'gwpzlakfcirfhkfv')

server.send_message(msg)
print('Mail sent...')

server.quit()