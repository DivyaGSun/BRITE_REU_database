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
  <a  class="active" href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/match.py">Match Candidates to Faculty</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/finalmatch.py">Final Matches</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/help_admin.py">Help</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/about_admin.py">About/Contact</a>
  </div>''')


## Begin actual page
print("<h1>Final Candidate to Project Matching</h1>")
print("<h3>Select a project, then select the assigned student</h3>")
print('<h4>To view final results, please visit "Final Matches"</h4>')

projects = []
projects.append('No selection')
candidates = []
candidates.append('No selection')
p = '''SELECT project_name FROM Project'''
s = '''SELECT a.firstname, a.lastname FROM Candidate c JOIN Applicant a ON c.cid = a.aid'''

connection = sqlite3.connect('db/BRITEREU.db')
c = connection.cursor()
#try:
    #c.execute(p)
    #results = c.fetchall()
    #for row in results:
        #projects.append(row[0])
    #c.execute(s)
    #results = c.fetchall()
    #for row in results:
        #name = row[1] + ', ' + row[0]
        #candidates.append(name)
#except Exception:
    #print("<p><font> color=red><b>Error</b></font></p>")

## Make dropdown code
#def makeS(name,values):
    #SEL = '<select name="{0}">{1}</select>'
    #OPT = '<option value="{0}">{0}</option>'
    #return (SEL.format(name, ''.join(OPT.format(v) for v in values)))

## Dropdown selection form
#print('''<form name="cpref" form action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/match.py" method="GET" >
    #Project: %s
    #<br /><br />
    #Candidate: %s
    #<br /><br />
    #<input type = "submit" value = "Submit"/>
    #</form>''') %(makeS('proj', projects), makeS('can', candidates))


###################################################################
#input and make selections
#query to get candidate data for the rows
query1 = "SELECT cid, firstname, lastname FROM Applicant join Candidate on Applicant.aid=Candidate.cid;"

#query to get the faculty and project names for the table headers
query2 = 'SELECT pid, uid, fname || " " || lname || ":\n" || project_name FROM Project JOIN User using(uid);'

#query to get all current candidate-faculty pairs in the database
query3 = 'SELECT cid || "_" || pid FROM Match ORDER BY(cid);'

#start connection
connection = sqlite3.connect('db/BRITEREU.db')
c = connection.cursor()
try:
    #execute query 1 
    c.execute(query1)
    #get results to above standard query
    results1 = c.fetchall()
except Exception:
    print("<p><font color=red><b>Error Query 1</b></font></p>")

try:
    #execute query 2
    c.execute(query2)
    #get results to above standard query
    results2 = c.fetchall()
except Exception:
    print("<p><font color=red><b>Error Query 2</b></font></p>")

try:
    #execute query 3
    c.execute(query3)
    #get results to above standard query
    results3 = c.fetchall()
except Exception:
    print("<p><font color=red><b>Error Query 3</b></font></p>")

c.close()
connection.close()


#get all the candidate-faculty pair ids currently in the database which will be used in the section that checks and uses form data
cfids = [cf[0] for cf in results3]

#retrieve form data
form = cgi.FieldStorage()

if form:
     res3 = [pair for pair in cfids]
     pairlist = form.getlist("cf")
     #find pairs that are in the selected list (pairlist) and not in the current database list (res3)
     tobe_inserted = list(set(pairlist) - set(res3))
     tobe_inserted = [tuple(i.split("_")) for i in tobe_inserted]
     #find pairs that are not in the selected list(pairlist) and are in the current database list (res3)
     tobe_removed = list(set(res3) - set(pairlist))
     tobe_removed = [tuple(map(int, i.split("_"))) for i in tobe_removed]
     if tobe_inserted or tobe_removed:
         connection = sqlite3.connect('db/BRITEREU.db')
         c = connection.cursor()
         for pair in tobe_inserted:
             insertStatement = "INSERT INTO Match(cid, pid) VALUES (%s, %s);" % pair
             c.execute(insertStatement)
             connection.commit()
         for pair in tobe_removed:  
             deleteStatement = 'DELETE FROM Match WHERE cid ="%s" and pid ="%s";' % pair
             c.execute(deleteStatement)
             connection.commit()
         c.close()
         connection.close()


#query the database again to now get all updated pairs
query4 = 'SELECT cid || "_" || pid FROM Match ORDER BY(cid);'

connection = sqlite3.connect('db/BRITEREU.db')
c = connection.cursor()
try:
    #execute query 1 
    c.execute(query4)
    #get results to above standard query
    results4 = c.fetchall()
except Exception:
    print("<p><font color=red><b>Error Query 4</b></font></p>")


#form action for user to submit checkboxes selections 
print('''<form name="form1" id="form1" action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/match.py" method="post" >''')
print('<table id=Candidate class="dataframe">')
print("<tr><th>Candidate ID</th><th>Candidate Name</th>")

#gets list of faculty
#adds all the faculty who are in the database as columns
for faculty in results2:
    print("<th>%s</th>") % faculty[2]
print("</tr>")


#get the Project IDs for the projects so that you concatenate to the CID to formulate a value pair
pids = [faculty[0] for faculty in results2]

#added proper URL for reference to reviewer page
#print the candidate table with a checkbox for each faculty member
for row in results1:
    print('''<tr><td><a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/reviewer.py?AID=%s">%s</a></td><td>%s %s</td>''') % (row[0], row[0], row[1], row[2]) 
    for f in pids:
        for cf_pair in results4:
            if (str(row[0])+"_"+str(f)) in cf_pair:
                print('<td><input title="GMT" type="checkbox" name="cf" value=%s checked="checked" /></td>') %  (str(row[0])+"_"+str(f))
                break
        else:
            print('<td><input type="checkbox" name="cf" value=%s /></td>') %  (str(row[0])+"_"+str(f))
    print("</tr>")


#add submit button for assigning faculty to candidates
print('<input type="submit" value="Make Matches" /><br /><br />')

#end form
print("</form>")

###################################################################
#Grid of ranking numbers
connection = sqlite3.connect('db/BRITEREU.db')
c = connection.cursor()


try:
    print("<table id=Candidate Ranks>")
    print("<tr><th>Candidate</th><th>Project name</th><th>Rank of proj</th><th>Faculty on proj</th><th>Rank of candidate</th></tr>")
    query = '''SELECT a.firstname || " " || a.lastname, p.project_name, cr.rank, u.fname || " " || u.lname, fr.rank
               FROM CandPref cr LEFT JOIN Faculty_Rank_Can fr USING (cid)
               LEFT JOIN Candidate c USING (cid) 
               LEFT JOIN Applicant a ON a.aid = c.cid 
               LEFT JOIN Project p USING (pid) 
               LEFT JOIN User u USING (uid);'''
    c.execute(query)
    r = c.fetchall()
    for row in r:
        print("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" %(row[0], row[1], row[2], row[3], row[4]))

except Exception:
    print("<p><font><b>Error</b></font></p>")
    
print("<h3>Rankings</h3>")

c.close()
connection.close()

print("</body></html>")

