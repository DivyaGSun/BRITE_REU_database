#!/usr/bin/python

import sys
import cgi
import cgitb
import sqlite3
reload(sys)
sys.setdefaultencoding('utf-8')
cgitb.enable()

# html
print("Content-type: text/html\n")
print('<meta charset="utf-8">')
print("<html><head>")
print("<title>BRITE REU Applicants</title>")
print('''<link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/nav.css">
         <link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/appadmin.css">

</head>''')


print("<body>")
print('''<div id ="topnav">
  <a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/rank_can.py">Rank Candidates</a>
  <a class="active" href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/finalmatch-fac.py">Your Candidates</a>
  <a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/help_fac.py">Help</a>
  <a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/about_fac.py">About/Contact</a>
</div>''')
  
print("<h1>Final Candidate and Project Matches</h1>")

print('<h3>To make changes, please visit "Match Candidates to Faculty"</h3>')

connection = sqlite3.connect('db/BRITEREU.db')
c = connection.cursor()

###TO UPDATE WITH LOGIN STUFF WORKING###
uid = 13
########################################

try:
    print("<table id=Candidate Ranks>")
    print("<tr><th>Candidate</th><th>Project name</th><th>Faculty on project</tr>")
    query = '''SELECT a.firstname || " " || a.lastname, p.project_name, u.fname || " " || u.lname
               FROM Match JOIN Applicant a ON aid=cid JOIN Project p USING (pid) JOIN User u USING (uid)
               WHERE u.uid LIKE "%s";''' %uid
    c.execute(query)
    r = c.fetchall()
    for row in r:
        print("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" %(row[0], row[1], row[2]))

except Exception:
    print("<p><font><b>Error</b></font></p>")
    

c.close()
connection.close()

print("</body></html>")