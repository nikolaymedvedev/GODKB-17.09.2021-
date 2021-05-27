import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
fromaddr = "nikolmedvedev123@gmail.com"
toaddr = "yavgenvovnov@gmail.com"
mypass = "135312345WnonW"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Привет от питона"
 
body = "Это пробное сообщение"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

