#!/usr/bin/python3.7

# Turn on debug mode.

import requests
import cgitb, cgi
cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
mail = form.getvalue('email')
opswd = form.getvalue('password')
redirectURL = "http://localhost:80/"

# Print necessary headers.
print('Content-Type: text/html\n\n')

if 'email' not in form or 'password' not in form:
    print('<meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 

else:
    print("""
    <br><br><form align= 'center' action='update_token.py'   method="post">
        <h3 >Hi """+str(mail)+"""   Please reset your password</h3> <br>
    Enter your new password:<input type='password' name= 'npswd'>
    <input type="hidden" name="mail" value="""+str(mail)+""">
    <input type="hidden" name="opswd" value="""+str(opswd)+""">
    <br> <input type='submit' value='reset'>
</form>""")

