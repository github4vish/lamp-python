#!/usr/bin/python
# Turn on debug mode.
import cgitb, cgi
cgitb.enable()


# Print necessary headers.
print("Content-Type: text/html")
print("""

 
<!DOCTYPE html>
<html>
<head>
<title>Portal</title>
</head>
<body>
<br>
<br>
<form align= 'center' action="validate.py" method="post">
   Email: <input type="email" name="email"><br><br>

 Password: <input type="password" name="password">
   <input type="submit" value="go">
</form>




""")




