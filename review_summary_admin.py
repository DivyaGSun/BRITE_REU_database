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
print("<title>Review Summary</title>")
print('''<link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/reviewer.css">''')
print('''<link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/nav.css">''')


print('''<style>
body {margin:30;padding:30;}
</style> </head>''')

print("<body>")
print('''<div id="bg-image">''')
print('''<div id ="topnav">
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/show_applicant_admin.py">Applicant List</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/stats_admin.py">Applicant Statistics</a>
  <a  href=""> Assign Users</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/input_projects.py">Input Faculty Projects</a>
  <a  class = "active" href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/review_summary_admin.py">View All Past Reviews</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/assign_candidate.py">Assign Candidates to Faculty</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/can_pref.py">Candidate Preferences</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/match.py">Match Candidates to Faculty</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/finalmatch.py">Final Matches</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/help_admin.py">Help</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/about_admin.py">About/Contact</a>
  </div>''')


print("<h1> Review Summary</h1>")
print("<h2> All Previously Submitted Reviews </h2>")
		

#print("<h2>%s's Past Reviews </h2>" %(fname))
print('''<form name="ReviewForm" action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/review_summary_admin.py" method="post" >
		<input type="hidden" id="id" name="uid" /><br>
		</form>''')
	
	

	
#create table
print("<table id=Applicant>")
#create table headers
print('''<tr><th>Applicant Name</th><th>Reviewer Name</th><th>Rank</th><th>Review</th><th>Date Submitted</th></tr>''')

connection = sqlite3.connect('db/BRITEREU.db')
c = connection.cursor() 

#query to retrieve the user's id 
query1 = '''select a.firstname, a.lastname, uid, reviews, created_at
from Applicant a join Review using(aid) 
order by created_at desc'''




c.execute(query1)
results = c.fetchall()
for row in results:
	print('''<tr><td>%s %s</td><td>%s </td><td> </td><td>%s</td><td>%s</td></tr>''' %(row[0], row[1], row[2], row[3], row[4]))

c.close()
connection.close()	

print("</table>")




print('''<script src="https://bioed.bu.edu/students_21/group_proj/group_K/tablefilter/tablefilter.js"></script>''')
print('''<script data-config="">
 var filtersConfig = {
     base_path: 'https://bioed.bu.edu/students_21/divyas3/tablefilter/',
  auto_filter: {
                    delay: 110 //milliseconds
              },
              filters_row_index: 1,
              state: true,
              alternate_rows: true,
              rows_counter: true,
              btn_reset: true,
              status_bar: true,
              msg_filter: 'Filtering...'
            };
            var tf = new TableFilter(Applicant, filtersConfig);
            tf.init();
          </script>''')


print("</body></html>")
