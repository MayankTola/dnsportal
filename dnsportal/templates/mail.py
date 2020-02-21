import os
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email import encoders
import datetime

date=datetime.datetime.now()
curr_month=date.strftime("%b")

curr_year=(date.strftime("%Y"))
file=str(curr_year + "-" + curr_month)
#print(file)
dir="/data/scripts/Yearly/{}/".format(file)
print(dir)
#files=["cpu.txt", "memory.txt","connection.txt"]


msg= MIMEMultipart()
msg["Subject"]= "Reports"
msg["From"] = "tngnoc_IIPMS_alert@airtel.com"
recipts=["tngnoc.udnssupport@airtel.com", "nandkishore.batra@airtel.com"]
msg["To"]= ",".join(recipts)

msg.attach(MIMEText("Monthly Reports attached"))

for file in os.listdir(dir):
        f= open(dir + file, 'rb')
        attach=MIMEText(f.read())
        f.close()

        attach.add_header('Content-Disposition', 'attachment' , filename=file)

        msg.attach(attach)

        print("Files attached")

#server setup
s=smtplib.SMTP("10.56.131.8")
#s.set_debuglevel(True)
s.sendmail("tngnoc.IIPMS_alert@airtel.com","tngnoc.udnssupport@airtel.com",msg.as_string())
s.quit()
print("Sent mail successfully")
