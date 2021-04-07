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
print("<html><head>")
print('''<style>
body {margin:30;padding:30;}

h1 {
  font-size: 30px;
  color: #000;
  border-bottom: 2px solid #ccc;
  padding-bottom: 5px;
}

label {display:block;}
textarea {display:block;}

#Applicant {
        font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
        border-collapse: collapse;
        width: 50%;
}

#Applicant td, #Applicant th {
        border: 1px solid #ddd;
        padding: 8px;
}

#Applicant th {
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: left;
        background-color: #5C30B2;
        color: white;
}
</style>

</head>''')

print("<body>")
print("<h1>Applicant Information</h1>")

print('''<form name="myForm" form action="https://bioed.bu.edu/cgi-bin/students_21/divyas3/reviewer.py" method="post" >
		<input type ='hidden' id='ID' name="AID" >

        <label for="Review">Review of Applicant:</label>
        <textarea id="Review" name="Review" rows="20" cols="80" ></textarea>
        <input type="submit" value="Submit">
		</form>''')

# get the form
form = cgi.FieldStorage()
# get three values from the form
AID = form.getvalue('AID')
Rev = form.getvalue('Review')

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

#if Rev:
    #'''query = UPDATE reviews set review = %s where aid =%s'''(%Rev, %AID)
    #print("<h2>Thanks your Review for Applicant Id %s have been recorded!</h2>" %AID)
c.close()
connection.close()
print("</table>")
#add reviewers past information
print("</body></html>")
