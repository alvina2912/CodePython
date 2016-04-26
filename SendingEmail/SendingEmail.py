import smtplib
sender='alvina2912@gmail.com'
receiver='alvina2912@gmail.com'
msg="Hello...This is test msg"

smtpobj=smtplib.SMTP("smtp.gmail.com",587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.ehlo()
smtpobj.login("alvina2912@gmail.com",'******')
smtpobj.sendmail(sender,receiver,msg)
print "Susscesfully email send"
smtpobj.close()
