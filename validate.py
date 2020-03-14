#!/usr/bin/python3.7

# Turn on debug mode.
import requests
import cgitb, cgi
cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
mail = form.getvalue('email')
pswd = form.getvalue('password')
redirectURL = "http://localhost:80/"

# Print necessary headers.
print('Content-Type: text/html\n\n')

if 'email' not in form or 'password' not in form:
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
    sql="select * from users  where email= %s and pswd= %s" 
    mycursor.execute(sql, (mail, pswd))
    
    myresult= mycursor.fetchone()
    #print( myresult )


    if mycursor.rowcount == 1 and myresult[1]== mail and myresult[2]== pswd and myresult[3]==1:
        url = str(redirectURL)+'reset.py'
        myobj = { 'email': mail, 'password': pswd}
        x = requests.post(url, data = myobj)
        print(x.text)


    if mycursor.rowcount == 1 and myresult[1]== mail and myresult[2]== pswd and myresult[3]==0:
        print ("<h1> Welcome  " +str(mail)+ " to the Portal </h1> ")

    if mycursor.rowcount == 1 and myresult[1]== mail and myresult[2]!= pswd:
        url = str(redirectURL)
        myobj = { 'wp': wp}
        x = requests.post(url, data = myobj)
        print(x.text)

    if mycursor.rowcount <= 0:
        import send_email as e
        e.token_email(mail)
        token= e.token
        print('We sent a mail<br>')
        
        sql = "INSERT INTO users (email, pswd) VALUES (%s, %s)"
        val = (mail, token)
        
        mycursor.execute(sql, val)
        
        mydb.commit()

        print('We generated token for you <br> please Check your mail for further insructions')
