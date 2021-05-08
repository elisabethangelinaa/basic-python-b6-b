import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr ="elisabeth.latianpython@gmail.com"
toaddr = "elisabethangelina14@gmail.com"

msg = MIMEMultipart ()

msg['From']=fromaddr
msg['To']=toaddr
msg['Subject']="Subject"

body ="Text"

msg.attach(MIMEText(body,'plain'))

server=smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Jamesangel1")
text= msg.as_string()
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print("Successfully sent to: ", msg['To'])


