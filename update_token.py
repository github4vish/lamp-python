#!/usr/bin/python

# Turn on debug mode.
import cgitb, cgi
cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
mail = form.getvalue('mail')
oldpswd = form.getvalue('opswd')
newpswd = form.getvalue('npswd')
token = 0
redirectURL = "http://localhost:80/"

# Print necessary headers.
print('Content-Type: text/html\n\n')

if 'opswd' not in form:
    print('<meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 

else:
    
# Connect to the database.
    import mysql.connector
    
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='password',
        database='portal'
        )
    
    mycursor = mydb.cursor()
    sql="update users  set pswd= %s , token =%s where pswd= %s and email= %s" 
    mycursor.execute(sql, (newpswd, token, oldpswd, mail))
    
    mydb.commit()
    
    print ("<h1> Welcome   "+str(mail)+ " to the Portal </h1> ")
