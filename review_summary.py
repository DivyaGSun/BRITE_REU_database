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
print("<title>BRITE REU Applicants</title>")
#print('''<link rel="stylesheet" href="/home/assets/css/bootstrap.min.css>''')
print('''<style>
body {margin:30;padding:30;}
h1 {
  font-size: 30px;
  color: #000;
  border-bottom: 2px solid #ccc;
  padding-bottom: 5px;
}
#ReviewSummary {
        font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
        border-collapse: collapse;
        width: 50%;
}
#ReviewSummary td, #Applicant th {
        border: 1px solid #ddd;
        padding: 8px;
}
#ReviewSummary tr:nth-child(even){background-color: #f2f2f2;}
#ReviewSummary tr:hover {background-color: #ddd;}
#ReviewSummary th {
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: left;
        background-color: #5C30B2;
        color: white;
}
</style> </head>''')

print("<body>")
print("<h1> Review Summary</h1>")
		

print("<h2>%s's Past Reviews </h2>" %(fname))
print('''<form name="ReviewForm" action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/review_summary.py" method="post" >
		<input type="hidden" id="id" name="uid" /><br>
		</form>''')
	
	
	
#must update to get hidden values ****
#get form values 
form = cgi.FieldStorage()
firstname = form.getvalue("firstname")
lastname = form.getvalue("lastname")	
	
#create table
print("<table id=ReviewSummary>")
#create table headers
print('''<tr><th>Reviewer ID</th><th>Applicant ID</th><th>Review</th></tr>''')

#<th>Date Submitted</th>


#query to retrieve the user's id 
query1 = '''select uid, aid, reviews
			from Review'''			

connection = sqlite3.connect('BRITEREU.db')
c = connection.cursor() 
#c.execute(query1)
#rid = c.fetchone()

#query to retrieve the review information 
#query2 = '''select *
#		from Review 
#		where rid = "%"''' %rid


c.execute(query1)
results = c.fetchall()
for row in results:
	print('''<tr><td>%s</td><td>%s</td><td>
			<div class="popop" onclick="myFunction()">Review
				<span class="popuptext" id="myPopup">%s</span>
			</div> 
			</td></tr>''' %(row[0], row[1], row[2]))

c.close()
connection.close()	

print("</table>")
#print('''
#<DIV id='PopUp' style='display: none; position: absolute; left: 100px; top: 100px; border: solid black 1px; padding: 10px; background-color: rgb(200,100,100); text-align: justify; font-size: 12px; width: 135px;' 
#onmouseclick="document.getElementById('PopUp').style.display = 'none' ">
#<SPAN id='PopUpText'>TEXT</SPAN>
#</DIV>>')

print("</body></html>")
