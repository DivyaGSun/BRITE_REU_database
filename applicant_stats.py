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
print("<html><head>")
print('''

<link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/nav.css">
<link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/reviewer.css">

</head>''')
print("<body>")
print('''<div id="bg-image">''')
print('''<div id ="topnav">
  <a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/show_applicant.py">Applicant List</a>
  <a class="active" href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/applicant_stats.py">Applicant Statistics</a>
  <a href="#about">My Past Reviews</a>
  <a href="#contact">About/Contact</a>

</div>''')

print("</body></html>")
