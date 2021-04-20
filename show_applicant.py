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
  <a  href="#contact">About/Contact</a>

</div>''')
print("<h1>Applicant Information</h1>")
print("<h3>Select applicant ID to write review | Click on ? for types of Filtering</h3>")
#did not include form action right now
#print('''<form action="https://bioed.bu.edu/cgi-bin/students_21/jpatel2/show_applicant.py" method="post" >
# </form>''')
print('<table id= Applicant class="dataframe">')
print("<tr><th>Applicant ID</th><th>Full Application</th><th>First Name</th><th>Last Name</th><th>Country</th><th>First Gen</th><th>School</th><th>Standing</th><th>Major</th><th>GPA</th><th>Date Submitted</th><th>Review Status</th></tr>")

#query to print applicant data
query1 = "SELECT aid, documents, firstname, lastname, country, firstgen, institution, standing, major, gpa, submitdate, reviewstatus FROM Applicant;"


connection = sqlite3.connect('db/BRITEREU.db')
c = connection.cursor()
try:
    #execute query
    c.execute(query1)
    #get results to above standard query
    results = c.fetchall()

except Exception:
    print("<p><font> color=red><b>Error</b></font></p>")

#added proper URL for reference to reviewer page
for row in results:
    print('''<tr><td><a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/reviewer.py?AID=%s">%s</a></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>''' % (row[0],row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],row[9], row[10], row[11]))
c.close()
connection.close()

print("</table>")
#print("</body>")
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

print("</body> </html>")
#print("</html>")
