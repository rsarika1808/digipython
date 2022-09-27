from re import S
import smtplib
gmail_user_='your_email@gmail.'
gmail_password='your_password.'
sent_from ='gmail_user'
to=['person_a@gmail.com','person_b @ gmail.com']
subject="lorem ipsam dolor sit amet"
body="consectetur adipiscing elit"
email_text =""\
from: % s
to: % s 
subject:% s 
% s 
""%("sent_from,","join(to),subject,body")
fry:
smtp_server =smtplib.SMTP_SSL
('smtp.gmailcom',465)
smtp_server.login('gmail_user_,gmail_password password')
smtp_server.sendmail(sent_from,to,email_text)
smtp_server.close()
print("Email sent successfully")
'except Exception as ex':
    print("something went wrong--")

