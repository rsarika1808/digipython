from email import message
import smtplib 
#Geates. SMTP(rathor.sarika1808@gmail.com)
#start TLS for securing.
smtplib.starttle()
#Authentication
smtplib.login("sender_ email_id", "sender_email_id_password")
#message to be sent.
message ="Message_you_need_to_send"
#sending the mail
smtplib.sendmail ="MEssage_ you_need_to_send"
#sending the mail
smtplib.sendmail("sender_email_id","receiver_email_id",message )
#terminating the session
smtplib.quit()
 






