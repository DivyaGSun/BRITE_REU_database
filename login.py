#!/usr/bin/python
import sys
import cgi
import cgitb
import sqlite3
reload(sys)
import traceback

sys.setdefaultencoding('utf-8')

cgitb.enable()

print("Content-type: text/html\n")
print('<meta charset="utf-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1">')
print("<html><head>")

print('''

<link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/login.css">''')

print('''<style>

#my_form p:nth-child(3){
    float: left !important;
    width: 50% !important;
}
#my_form p:nth-child(4) {
    float: right !important;
    width: 50% !important;
}

</style></head>''')


print("<body>")
print('''
<form id="my_form" form action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/login.py" method="post">
    <p class="clearfix">
        <label for="login">Username</label>
        <input type="text" name="login" id="login" placeholder="Username">
    </p>
    <p class="clearfix">
        <label for="password">Password</label>
        <input type="password" name="password" id="password" placeholder="Password">
    </p>
    <p class="clearfix">
        <input type="submit" name="submit" value="Sign in">
    </p>
    <p class="clearfix">
        <input type="button" value="Create Account" onclick = "location.href='https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/create_account.py'">
    </p>
</form>

''')

print("</body></html>")
#cur.execute("SELECT Password FROM Users WHERE Username = ?", (un,))
