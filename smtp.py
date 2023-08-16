"""sending email using python"""
import smtplib

#std port for encryption TLS

smt_obj=smtplib.SMTP('smtp.ymail.com',587)
smt_obj.ehlo()
smt_obj.starttls()
sender='patelbhakti234@gmail.com'
receiver= 'bpatel92@ymail.com'
smt_obj.login('patelbhakti234@gmail.com','Luisenplatz24')
smt_obj.sendmail(sender,receiver,'Subject:SMTP message.\n This is a test email.')
smt_obj.close()  #\n