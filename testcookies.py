#!/usr/bin/python
import os
def test_cookies():
    print("Set-Cookie:UserID = XYZ;\r\n")
    print("Set-Cookie:Password = XYZ123;\r\n")
    print("Set-Cookie:Expires = Tuesday, 31-Dec-2007 23:12:40 GMT;\r\n")
    print("Set-Cookie:Domain = www.tutorialspoint.com;\r\n")
    print("Content-type:text/html\r\n\r\n")
    print('<html>')
    print('<head>')
    print('<title>COOKIES SET - First CGI Program</title>')
    print('</head>')
    print('<body>')
    print('<h2>ALL Done!</h2>')
    print('</body>')
    print('</html>')
    for param in os.environ.keys():
        if (param=="HTTP_COOKIE"):
            print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

test_cookies()
for param in os.environ.keys():
    if(param=="HTTP_COOKIE"):
        print("<b>%20s</b>: %s<br>" % param, os.environ[param])