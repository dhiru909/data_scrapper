from base64 import encode
from pydoc import plain
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
def send(filename):
    
    msg=MIMEMultipart()

    subject="Stock Report"
    from_add='brainyplays222@gmail.com'
    to_add='dhirajkhali1@gmail.com'
    msg['From']=from_add
    msg['To']=to_add
    msg['Subject']=subject
    body="Todays Stock Report"
    msg.attach(MIMEText(body,'plain'))

    my_file=open(filename,'rb')
    part=MIMEBase('application','octet-stream')
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment; filename= '+ filename)
    msg.attach(part)

    message=msg.as_string()
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(from_add,'ealfqbpcilxnvbmz')
    server.sendmail(from_add,to_add,message)
    server.quit()