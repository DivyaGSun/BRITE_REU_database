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
print("<title>Faculty Help Page</title>")
print('''</head>''')

print("<body>")
print('''<div id="bg-image">''')
print('''<div id ="topnav">
  <a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/rank_can.py">Rank Candidates</a>
  <a class = "active" href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/help_fac.py">Help</a>
  <a href="#contact">About/Contact</a>
</div>''')
print('''<h1>Faculty: Help Page</h1>
<h2>For help using webpages see below:</h2>
<h3>Rank Candidates Page: </h3>
<p>To view candidates' application documents, please click on hyperlinks below ranking form. <br />
	Once you have reviewed the candidates' applications, please choose your top candidates by ranking from 1 to 5.<br />
	1 being the highest and 5 being the lowest. <br />
	Using the radio button submit form, please choose only one candidate per rank(1-5). <br />
	These rankings will be accounted for when assigning students to work with you on your projects. <br />
</p>

<h3>Please Note: </h3>
<p>Depending on your login role, you will only have access to certain pages. <br />
If you are struggling to gain correct access please contact the admin: Gary Benson, gbenson@bu.edu. <br />

Current Role: Faculty Member </p></body>''')
print("</html>")