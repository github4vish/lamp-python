#!/usr/bin/python3.7

import cgitb, cgi
cgitb.enable()

# Create instance of FieldStorage
# Get data from fields
mail = 'testmail.lamp@gmail.com'
redirectURL = "http://localhost:80/"


# Print necessary headers.
import secrets
token= secrets.token_urlsafe(10)
import smtplib
MY_ADDRESS = 'testmail.lamp@gmail.com'
PASSWORD = 'testmail4python@'
message = """From: From Portal 
To: To Person 
Subject: Login token generated. 
"""+str(token)+"""
login with this token and your email using this link.
"""
try:
    smtpObj = smtplib.SMTP(host='smtp.gmail.com', port='587')
    smtpObj.starttls()
    smtpObj.login(MY_ADDRESS, PASSWORD)
    
    smtpObj.sendmail(MY_ADDRESS, mail, message)         
    print ("We sent you a mail")
    smtpObj.quit()
    
    

except SMTPException:
    print ("Error: unable to send email")
finally:
    
    print('Content-Type: text/html\n\n')
    # Connect to the database.
    import mysql.connector
    
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='password',
        database='portal'
        )
    
    mycursor = mydb.cursor()
    sql = "INSERT INTO users (email, pswd) VALUES (%s, %s)"
    val = (mail, token)
    mycursor.execute(sql, val)
    
    
    mydb.commit()
    
    if mycursor.rowcount == 1:
        print ("Hi "+str(mail)+"<br> We have generated token for you to access portal <br> Please check your mail for further instructions")
