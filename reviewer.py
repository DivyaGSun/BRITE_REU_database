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
print("<h1>Submit a Review</h1>")

# print('''<form name="myForm" form action="https://bioed.bu.edu/cgi-bin/students_21/divyas3/reviewer.py" method="post" >
# 		<input type ='hidden' id='ID' name="AID" value = AID>
#
#         <label for="Review">Enter review of Applicant:</label>
#         <textarea id="Review" name="Review" rows="20" cols="80" ></textarea>
#         <input type="submit" onclick= "clicked()" value="Submit">
# 		</form>''')

# get the form
form = cgi.FieldStorage()
# get three values from the form
AID = str(form.getvalue('AID'))
Rev = form.getvalue('Review')
UID = str(0)
AIDs = str(AID)

#
print('''<form name="myForm" form action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/reviewer.py" method="GET" >
		<input type ='hidden' id='ID' name="AID" value = %s>

        <label for="Review">Enter review of Applicant:</label>
        <textarea id="Review" name="Review" rows="20" cols="80" ></textarea>
        <input type="submit" onclick= "clicked()" value="Submit">
		</form>'''%(AID))

# AID = str(form.getvalue('AID'))
# Rev = str(form.getvalue('Review'))
# UID = str(0)
# AIDs = str(AID)

query1 = """SELECT aid, firstname, lastname, emailaddress, submitdate, reviewstatus
FROM Applicant
WHERE aid='%s';""" %(AID)

#connection = sqlite3.connect('/https://bioed.bu.edu/students_21/divyas3/BRITEREU.db')
connection = sqlite3.connect('db/BRITEREU.db')
c = connection.cursor()
try:
    #execute query
    c.execute(query1)
    #get results to above standard query
    results = c.fetchall()

except Exception:
    print("<p><font> color=red><b>Error</b></font></p>")

print("<h3>Applicant Information</h3>")
print("<table id=Applicant>")
print("<tr><th>Applicant ID</th><th>First Name</th><th>Last Name</th><th>Email Address</th><th>Date Submitted</th><th>Review Status</th></tr>")

for row in results:
    print('''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>''' % (row[0], row[1], row[2], row[3], row[4], row[5]))

print("</table>")
if Rev:
    print('true')
if Rev:
    print(AIDs)
    insert = "INSERT INTO Review (aid,uid,reviews) VALUES (?,?,?)"
    print(str(insert))
    try:
        c.execute(insert, (AIDs, UID , Rev))
        connection.commit()
    #except Exception as sqlError:
       # print(sqlError)
	#print(str(AID))
        #print(str(UID))
        #print("|%s|"%(Rev))
    except sqlite3.Error as er:
    	print('SQLite error: %s' % (' '.join(er.args)))
    	print("Exception class is: ", er.__class__)
    	print('SQLite traceback: ')
    	exc_type, exc_value, exc_tb = sys.exc_info()
    	print(traceback.format_exception(exc_type, exc_value, exc_tb))
        print(str(AID))
        print(str(UID))
        print("|%s|"%(Rev))
    # prnt("<h2>Thanks your Review for Applicant Id %s have been recorded!</h2>" %AIDs)
    # query2 = "UPDATE Applicant set reviewstatus = Completed"
    # c.execute(query)


c.close()
connection.close()
#print("</table>")

print('Link to download full application:---(hyperlink this)')
#add reviewers past information
print("<h3>Previous Reviews Completed</h3>")

print('''<script type="text/javascript">
    function clicked() {
       if (confirm('Do you want to submit?')) {
           submit.submit();
       } else {
           return false;
       }
    }

</script>''')
print("</body></html>")
