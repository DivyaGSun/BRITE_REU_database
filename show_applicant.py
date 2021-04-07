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
#Applicant {
        font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
        border-collapse: collapse;
        width: 50%;
}

#Applicant td, #Applicant th {
        border: 1px solid #ddd;
        padding: 8px;
}

#Applicant tr:nth-child(even){background-color: #f2f2f2;}

#Applicant tr:hover {background-color: #ddd;}

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
print("<h3>Select applicant ID to write review</h3>")
#did not include form action right now
#print('''<form action="https://bioed.bu.edu/cgi-bin/students_21/jpatel2/show_applicant.py" method="post" >
# </form>''')
print('<table id= Applicant class="dataframe">')
print("<tr><th>Applicant ID</th><th>First Name</th><th>Last Name</th><th>Email Address</th><th>Date Submitted</th><th>Review Status</th></tr>")

#query to print applicant data
query1 = "SELECT aid, firstname, lastname, emailaddress, submitdate, reviewstatus FROM Applicant;"


connection = sqlite3.connect('BRITEREU.db')
c = connection.cursor()
try:
    #execute query
    c.execute(query1)
    #get results to above standard query
    results = c.fetchall()

except Exception:
    print("<p><font> color=red><b>Error</b></font></p>")

for row in results:
    print('''<tr><td><a href="https://bioed.bu.edu/cgi-bin/students_21/divyas3/reviewer.py?AID=%s">%s</a></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>''' % (row[0],row[0], row[1], row[2], row[3], row[4], row[5]))
c.close()
connection.close()

print("</table>")
#print("</body>")
print('''<script src="https://bioed.bu.edu/students_21/divyas3/tablefilter/tablefilter.js"></script>''')
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
