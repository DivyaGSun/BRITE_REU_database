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
print('''<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<body>
<div id="bg-image">
<div id ="topnav">
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/show_applicant_admin.py">Applicant List</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/stats_admin.py">Applicant Statistics</a>
  <a  href=""> Assign Users</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/input_projects.py">Input Faculty Projects</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/review_summary_admin.py">View All Past Reviews</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/assign_candidate.py">Assign Candidates to Faculty</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/can_pref.py">Candidate Preferences</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/match.py">Match Candidates to Faculty</a>
  <a  class="active" href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/finalmatch.py">Final Matches</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/help_admin.py">Help</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/about_admin.py">About/Contact</a>
  </div>''')
  
print("<h1>Final Candidate and Project Matches</h1>")

print('<h3>To make changes, please visit "Match Candidates to Faculty"</h3>')

connection = sqlite3.connect('db/BRITEREU.db')
c = connection.cursor()

try:
    print("<table id=Candidate Ranks>")
    print("<tr><th>Candidate</th><th>Project name</th><th>Faculty on project</tr>")
    query = '''SELECT a.firstname || " " || a.lastname, p.project_name, u.fname || " " || u.lname
               FROM Match JOIN Applicant a ON aid=cid JOIN Project p USING (pid) JOIN User u USING (uid);'''
    c.execute(query)
    r = c.fetchall()
    for row in r:
        print("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" %(row[0], row[1], row[2]))

except Exception:
    print("<p><font><b>Error</b></font></p>")
    

c.close()
connection.close()

print("</body></html>")