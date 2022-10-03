from http import server
import smtplib,_ssl
import ssl
post =465# for ss1
password =input("Type your password and press enter:")
#create a secure ss1 context
context =ssl. create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",'context =context'):
server.logic("my@gmail.com",password)
#TODO:send email here.


