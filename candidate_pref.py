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
print("<title>BRITE REU Applicants</title>")
print('''
      <link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/nav.css">
      <link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/reviewer.css">

</head>''')
print("<body>")
print('''<div id="bg-image">''')
print('''<div id ="topnav">
  <a class="active" href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/show_applicant.py">Applicant List</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/applicant_stats.py">Applicant Statistics</a>
  <a  href="#about">My Past Reviews</a>
  <a  href="#help">Help</a>
  <a  href="#contact">About/Contact</a>

</div>''')

print("<h1>Candidate Project Preferences</h1>")

print("<h3>Please input candidate ID and project preferences: 1 being the highest, 5 being the lowest</h3>")
 
print("<form name='Ranking' action='Submit' method='post'/>")
pnum = 5
pr = ['Project 1', 'Project 2', 'Project 3', 'Project 4', 'Project 5']

print('''<form name="drop3" form action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/candidate_pref.py" method="GET" >
    <input type="text" name="cid" id="cid" placeholder="Candidate ID" required><br /><br />
    1st choice: <select name = "dropdown">
    <option value = "No selection" selected>Select</option>
    <option value = "Project 1">Project 1</option>
    <option value = "Project 2">Project 2</option>
    <option value = "Project 3">Project 3</option>
    </select><br /><br />
    2nd choice: <select name = "dropdown2">
    <option value = "No selection" selected>Select</option>
    <option value = "Project 1">Project 1</option>
    <option value = "Project 2">Project 2</option> 
    <option value = "Project 3">Project 3</option>
    </select><br /><br />
    3rd choice: <select name = "dropdown3">
    <option value = "No selection" selected>Select</option>
    <option value = "Project 1">Project 1</option>
    <option value = "Project 2">Project 2</option>
    <option value = "Project 3">Project 3</option>
    </select>
    <input type = "submit" value = "Submit"/>
    </form>''')

# get the form
form = cgi.FieldStorage()
# get three values from the form
CID = str(form.getvalue('cid'))
r1 = form.getvalue('dropdown')
r2 = form.getvalue('dropdown2')
r3 = form.getvalue('dropdown3')

names = [r1, r2, r3]
pids = []


connection = sqlite3.connect('db/BRITEREU.db')
c = connection.cursor()
try:
    print("<table id=Candidate Ranks>")
    print("<tr><th>Candidate ID</th><th>Project ID</th><th>Rank</th></tr>")
    query = '''SELECT * FROM CandidatePref;'''
    c.execute(query)
    r = c.fetchall()
    for row in r:
        print("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" %(row[1], row[2], row[3]))

except Exception:
    print("<p><font><b>Error</b></font></p>")

c.close()
connection.close()

print("</body></html>")

