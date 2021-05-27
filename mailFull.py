import smtplib
import os
import mimetypes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(addr_to, msg_subj, msg_text, files):
    addr_from = "nikolmedvedev123@gmail.com"
    password  = "135312345WnonW"

    msg = MIMEMultipart()
    msg['nikolmedvedev123@gmail.com'] = addr_from
    msg['yavgenvovnov@gmail.com'] = addr_to
    msg['Тема'] = msg_subj

    body = msg_text
    msg.attach(MIMEText(body, 'Приветствую!!!'))

    process_attachement(msg, files)
    server = smtplib.SMTP_SSL('smtp.mail.ru', 587)
    server.login(addr_from, password)
    server.send_message(msg)
    server.quit()

def process_attachement(msg, files):
    for f in files:
        if os.path.isfile(f):
            attach_file(msg,f)
        elif os.path.exists(f):
            dir = os.listdir(f)
            for file in dir:
                attach_file(msg,f+"/"+file)

addr_to   = "bragin-crb@mail.gomel.by"
files = ["S:/Медперсонал/Эпикризы для отправки/Брагин ЦРБ/*"]

send_email(addr_to, "Выписные эпикризы", "Выписные эпикризы", files)