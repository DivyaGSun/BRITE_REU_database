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
print('''<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>''')

print('''<style>
body {margin:30;padding:30;}
</style> </head>''')

print("<body>")
print('''<div id="bg-image">''')
print('''<div id ="topnav">
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/show_applicant.py">Applicant List</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/stats.py">Applicant Statistics</a>
  <a  class = "active" href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/review_summary.py">My Past Reviews</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/help_reviewer.py">Help</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/about_rev.py">About/Contact</a>
  </div>''')

print("<h1> Review Summary</h1>")
print("<h2> My Past Reviews </h2>")
		

#print("<h2>%s's Past Reviews </h2>" %(fname))
print('''<form name="ReviewForm" action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/review_summary.py" method="post" >
		<input type="hidden" id="id" name="uid" /><br>
		</form>''')
	
	
	
#must update to get hidden values ****
#get form values 
#form = cgi.FieldStorage()
uid = 0
	
#create table
print("<table id=Applicant>")
#create table headers
print('''<tr><th>Applicant Name</th><th>Rank</th><th>Review</th><th>Date Submitted</th></tr>''')


#form = cgi.FieldStorage()
#uid = form.getvalue('uid')

#query to retrieve the user's id 
query1 = '''select firstname, lastname, reviews, created_at
			from Review join Applicant using(aid)
			where uid = %s
			order by created_at desc''' %uid	

connection = sqlite3.connect('db/BRITEREU.db')
c = connection.cursor() 


c.execute(query1)
results = c.fetchall()
for row in results:
	print('''<tr><td>%s %s</td><td> </td><td>
			<div contenteditable id="editor">%s
			</div>
			<button id="save">Click to Save</button>
			<script type="text/javascript">
				$(document).ready(function(argument) {
					$('#save').click(function(){
					// Get edit field value
						$edit = $('#editor').html();
						$.ajax({
							url: 'get.php',
							type: 'post',
							data: {data: $edit},
							datatype: 'html',
							success: function(rsp){
									alert(rsp);
							}
					});
				});
			}); 
			</script>
			<td>%s
			</td></tr>''' %(row[0], row[1], row[2], row[3]))
			
print('''<?php
$editData = $_POST['data'];

$db = new SQLite3('db/BRITEREU.db')

// Add your validation and save data to database

echo $editData;
?>''')
		
query2 = '''UPDATE Review
			SET reviews = review 
			'''

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
