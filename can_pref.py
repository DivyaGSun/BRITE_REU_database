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
  <a  class="active" href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/can_pref.py">Candidate Preferences</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/match.py">Match Candidates to Faculty</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/finalmatch.py">Final Matches</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/help_admin.py">Help</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/about_admin.py">About/Contact</a>
  </div>''')


## Begin actual page
print("<h1>Candidate Project Preferences</h1>")

print("<h3>Please select candidate name and project preferences</h3>")
 
print("<form name='Ranking' action='Submit' method='post'/>")

## Get all candidates and projects to populate the dropdowns
projects = []
projects.append('No selection')
candidates = []
candidates.append('No selection')
p = '''SELECT project_name FROM Project'''
s = '''SELECT a.firstname, a.lastname FROM Candidate c JOIN Applicant a ON c.cid = a.aid'''

connection = sqlite3.connect('db/BRITEREU.db')
c = connection.cursor()
try:
    c.execute(p)
    results = c.fetchall()
    for row in results:
        projects.append(row[0])
    c.execute(s)
    results = c.fetchall()
    for row in results:
        name = row[1] + ', ' + row[0]
        candidates.append(name)
except Exception:
    print("<p><font> color=red><b>Error</b></font></p>")

## Make dropdown code
def makeS(name,values):
    SEL = '<select name="{0}">{1}</select>'
    OPT = '<option value="{0}">{0}</option>'
    return (SEL.format(name, ''.join(OPT.format(v) for v in values)))

## Dropdown selection form
print('''<form name="cpref" form action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/can_pref.py" method="post"  >
    Candidate: %s
    <br /><br />
    1st choice: %s
    <br /><br />
    2nd choice: %s
    <br /><br />
    3rd choice: %s
    <br /><br />
    4th choice: %s
    <br /><br />
    5th choice: %s
    <br /><br />
    <input type = "submit" value = "Submit" />
    </form>''') %(makeS('can', candidates), makeS('p1', projects), makeS('p2', projects), makeS('p3', projects), makeS('p4', projects), makeS('p5', projects))

# get the form
form = cgi.FieldStorage()
# get three values from the form
name = str(form.getvalue('can'))
r1 = form.getvalue('p1')
r2 = form.getvalue('p2')
r3 = form.getvalue('p3')
r4 = form.getvalue('p4')
r5 = form.getvalue('p5')

names = [r1, r2, r3, r4, r5]
pids = []
if name != 'No selection' and name != None:
    for i in range(len(names)):
        if names[i] != 'No selection' and names[i] != None:
          q1 = '''SELECT pid FROM Project WHERE project_name LIKE "%s";'''%names[i]
          c.execute(q1)
          r = c.fetchall()
          pids.append(r)

    name2 = name.split(',')
    lname = name[0]
    fname = name[1]
    q2 = '''SELECT cid FROM Candidate JOIN Applicant ON aid=cid WHERE lastname LIKE "%s" AND firstname LIKE "%s";''' %(lname, fname)
    c.execute(q2)
    tid = c.fetchall()

    for j in range(len(pids)):
        q3 = '''INSERT INTO CandPref (cid, pid, rank) VALUES(%s, %s, %s);''' %(tid, pids[i], i+1)
        c.execute(q3)
        connection.commit()


##########################################
#print table

try:
    print('''<form name="form1" id="form1" action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/can_pref.py" method = "get">''')
    print("<h4>Removing a ranking removes all rankings for the selected candidate</h4>")
    print("<table id=Candidate Ranks>")
    print("<tr><th>Candidate</th><th>Project</th><th>Rank</th><th>Remove rank</th></tr>")
    query = '''SELECT a.firstname || " " || a.lastname, p.project_name, rank, cr.cid
               FROM CandPref cr 
               JOIN Applicant a ON a.aid = cr.cid
               JOIN Project p USING (pid)
               ORDER BY a.lastname, rank;'''
    c.execute(query)
    r = c.fetchall()
    for row in r:
        print("<tr><td>%s</td><td>%s</td><td>%s</td><td><input type='checkbox' name='rcan' value=%s /></td></tr>" %(row[0], row[1], row[2], row[3]))
    print('<input type="submit" value="Remove ranking" /><br /><br />')
    
    print("</form>")
    form = cgi.FieldStorage()

    if form:
        removelist = form.getlist("rcan")
        connection = sqlite3.connect('db/BRITEREU.db')
        c = connection.cursor()
        for candidate in removelist:
            deleteStatement = "DELETE FROM CanPref WHERE cid = %d;" % int(candidate)
            c.execute(deleteStatement)
            connection.commit()

except Exception:
    print("<p><font><b>Error</b></font></p>")

c.close()
connection.close()

print("</body></html>")
