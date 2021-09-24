#!/usr/bin/env python3
import cgi
import cgitb
import os
from secret import username, password
from templates import secret_page, after_login_incorrect

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
input_username = form.getvalue('username')
input_password = form.getvalue('password')

if username == input_username and password == input_password:
    # if the input account is correct
    print("Content-type:text/html")
    print(f"Set-Cookie:loginCorrect = True\r\n")
    print("<html>")
    print("<head>")
    print("<title>Hello - Second CGI Program</title>")
    print("</head>")
    print("<body>")
    print("<p><b>Username</b> %s <b>password</b> %s</p>" % (input_username, input_password))
    print("</body>")
    print("</html>")
    # check if account is logged in, if yes, display secret message
    for param in os.environ.keys():
        if (param == "HTTP_COOKIE"):
            cookie_parameter = os.environ[param]
            if 'loginCorrect=True' in cookie_parameter:
                print(secret_page(username, password))
else:
    print(after_login_incorrect())

