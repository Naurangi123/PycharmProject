import smtplib

my_mail="rahulkumar4817@gmail.com"
password="rahul$$##@4817"


connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_mail,password=password)
connection.sendmail(from_addr=my_mail,to_addrs="naurangilal9675329115@gmail.com",msg="Hello")
connection.close()