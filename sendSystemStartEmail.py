import smtplib
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import subprocess
import datetime
import os

def wait_for_internet():
    while True:
        try:
            socket.create_connection(("www.google.com",80))
            return
        except OSError:
            pass

#check internet connection
wait_for_internet()

fp = open("/root/scripts/creds.data","r")

addr = fp.readline().strip() #from email
toaddr = addr #to email
password = fp.readline().strip() #your password/app password

fp.close()

time=str(datetime.datetime.now())
netinfo=subprocess.run(["/usr/bin/ip","link"], stdout=subprocess.PIPE).stdout.decode('utf-8')
iwinfo=subprocess.run(["/usr/bin/iw","dev"], stdout=subprocess.PIPE).stdout.decode('utf-8')
winfo=subprocess.run(["/usr/bin/w"], stdout=subprocess.PIPE).stdout.decode('utf-8')
sysname = os.uname()[1]
message="The system "+sysname+" has been turned on.\nTimestamp: "+str(datetime.datetime.now())+"."
message+="\nip link output:\n "+netinfo
message+="\niw dev output:\n "+iwinfo
message+="\nw output:\n"+winfo

s = smtplib.SMTP(host="smtp.gmail.com",port=587)
s.starttls()
s.login(addr, password)

msg = MIMEMultipart()

msg['From']=addr
msg['To']=toaddr
msg['Subject']=sysname+": System has been turned on"

msg.attach(MIMEText(message, 'plain'))

s.send_message(msg)

del msg

#s.sendmail(addr,addr,"testmessage")

s.quit()
