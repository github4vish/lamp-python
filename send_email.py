#!/usr/bin/python3.7

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import secrets

token= secrets.token_urlsafe(10)
MY_ADDRESS = 'testmail.lamp@gmail.com'
PASSWORD = 'testmail4python@'
redirectURL= 'http://localhost:80'

def token_email(email):
    
    # set up the SMTP server
    smtpObj = smtplib.SMTP(host='smtp.gmail.com', port='587')
    smtpObj.starttls()
    smtpObj.login(MY_ADDRESS, PASSWORD)
    
    
    msg = MIMEMultipart()       # create a message

    message = """ <h1> """+str(token)+""" </h1>
    login with this token and your email using this link.
    
    <a href='"""+str(redirectURL)+"""'>Portal Login</a>  """

    msg['From']= MY_ADDRESS
    msg['To']= email
    msg['Subject']= "Login token Generated"
    
       
    # add in the message body
    msg.attach(MIMEText(message, 'html'))
    
    # send the message via the server set up earlier.
    smtpObj.send_message(msg)
    del msg

    smtpObj.quit()
    

