#!/usr/bin/python
import sys
import cgi
import cgitb
import sqlite3
reload(sys)
#import sys
sys.setdefaultencoding('utf-8')

cgitb.enable()

print("Content-type: text/html\n")
print('<meta charset="utf-8">')

print("<body>")
print("<h1>Reviewer Information</h1>")

print('''<form name="myForm" form action="https://bioed.bu.edu/cgi-bin/students_21/divyas3/reviewer.py" method="post" >
		<input type ='hidden' id='ID' name="AID" >
		</form>''')


# get the form
form = cgi.FieldStorage()
# get three values from the form
AID = form.getvalue('AID')

query1 = """SELECT aid, firstname, lastname, emailaddress, submitdate, reviewstatus
FROM Applicant
WHERE aid='%s';""" %(AID)

connection = sqlite3.connect('BRITEREU.db')
c = connection.cursor()
try:
    #execute query
    c.execute(query1)
    #get results to above standard query
    results = c.fetchall()

except Exception:
    print("<p><font> color=red><b>Error</b></font></p>")

print("<table id=Applicant>")
print("<tr><th>Applicant ID</th><th>First Name</th><th>Last Name</th><th>Email Address</th><th>Date Submitted</th><th>Review Status</th></tr>")

for row in results:
    print('''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>''' % (row[0], row[1], row[2], row[3], row[4], row[5]))
c.close()
connection.close()
print("</table>")
#add reviewers past information
print("</body></html>")
