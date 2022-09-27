email = input ('enter ur email')
if len(email)<11:
    print ('length of email not valid')
elif '.com'not in email and 'org'not in email:
    print ('invalid domain')
else :
    print ("your email look vaild")