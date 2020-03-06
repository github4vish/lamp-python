# lamp-python

#Purpose: 
Create an account on the portal for the new member by validating the existence of account from the backend

##Brief Description: 
An automatic email containing link to access portal with credentials has to be generated for a new member to login to the portal. The email has to be generated to the member by validating (whether the member already has an account in the portal – Validate the transactions in the database to see if the enrolment date is today) and generate the email to the account with following details –
    • Link to portal – Create a dummy login page and host it. Generate URL and this can be used as link to portal
    • Username – Email ID
    • Password – Generate Temporary Password
Once the user is successfully logged in, Prompt the user to change the password by redirecting to a page containing 3 fields as below –
    • Old password – Where temporary password to be used
    • New password – User need to input the new password
    • Confirm Password – User need to re-enter the password
Once these details are provided by the user and by clicking on submit - the respective record with the new password has to be updated in the database and the user should be allowed to view the welcome page.
Needs:
Front end Html pages –
    1. Login page with email & temp password
    2. Reset password page with old password, new password and temporary password
    3. Welcome page showing login successful
Database records with (SQL database)–
    1. Existing records who already has account on the portal
    2. New records for whom the account has to be created
These records are for validating the existence of user account and determine if it is a new record and eventually generate automatic email.
Backend functionality (Use Python) –
    1. Generate automatic email to the new user present in the database with link, username and password.



