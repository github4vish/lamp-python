#!/usr/bin/python

# Turn on debug mode.
import cgitb, cgi
cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
email = form.getvalue('email')
password = form.getvalue('password')


# Print necessary headers.
print("Content-Type: text/html")
print()


print("<br>")
print("<br>")
print("   Welcome %s    " % (email ))
print("<br>")
print("<br>")


# Connect to the database.
#import pymysql
#conn = pymysql.connect(
 #   db='example',
  #  user='root',
   # passwd='password',
   # host='localhost')
#c = conn.cursor()

# Insert some example data.
#c.execute("INSERT INTO numbers VALUES (1, 'One!')")
#c.execute("INSERT INTO numbers VALUES (2, 'Two!')")
#c.execute("INSERT INTO numbers VALUES (3, 'Three!')")
#conn.commit()

# Print the contents of the database.
#c.execute("SELECT * FROM numbers")
#print([(r[0], r[1]) for r in c.fetchall()])


 
