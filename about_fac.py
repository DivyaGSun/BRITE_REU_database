#!/usr/bin/python

import sys
import cgi
import cgitb
import sqlite3
reload(sys)
#import sys
sys.setdefaultencoding('utf-8')

cgitb.enable()

# html
print("Content-type: text/html\n")
print('<meta charset="utf-8">')
print("<html><head>")
print('''<link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/nav.css">''')
print('''<style>
body {margin:30;padding:30;}
</style> </head>''')
print("<title>Faculty Help Page</title>")
print('''</head>''')

print("<body>")
print('''<div id="bg-image">''')
print('''<div id ="topnav">
  <a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/rank_can.py">Rank Candidates</a>
  <a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/help_fac.py">Help</a>
  <a class = "active" href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/about_fac.py">About/Contact</a>
</div>''')
print('''
<h3>About: </h3>
<p>The BRITE REU Program is an NSF funded summer mentored research program for undergraduate students who work full time in a lab for ten weeks and participate in various training activities. 
The BRITE REU database is used to store all the applicant data. This website acts as a portal to the database information. 
This website allows applicants to be easily reviewed. This website also helps the admin to assign candidates to faculty projects. 
This database and website were created by BU Bioinformatics graduate students as apart of their coursework. 
The project was completed under the supervision of Gary Benson. </p>
<h3>Contact Information: </h3>
<p>Gary Benson: gbenson@bu.edu <br />
Divya Sundaresan: divyas3@bu.edu <br />
Marissa Chiaradio: mdc98@bu.edu <br />
Kenzie Knox: mfknox@bu.edu <br />
Janvee Patel: jpatel2@bu.edu </p>
</body>''')
print("</html>")