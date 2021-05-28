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
print('''<link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/nav.css">''')
print('''<style>
/* Popup container - can be anything you want */
.popup {
  position: relative;
  display: inline-block;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/* The actual popup */
.popup .popuptext {
  visibility: hidden;
  width: 160px;
  background-color: #555;
  color: #fff;
  text-align: center;
  border-radius: 6px;
  padding: 8px 0;
  position: absolute;
  z-index: 1;
  bottom: 125%;
  left: 50%;
  margin-left: -80px;
}

/* Popup arrow */
.popup .popuptext::after {
  content: "";
  position: absolute;
  top: 100%;
  left: 50%;
  margin-left: -5px;
  border-width: 5px;
  border-style: solid;
  border-color: #555 transparent transparent transparent;
}

/* Toggle this class - hide and show the popup */
.popup .show {
  visibility: visible;
  -webkit-animation: fadeIn 1s;
  animation: fadeIn 1s;
}

/* Add animation (fade in the popup) */
@-webkit-keyframes fadeIn {
  from {opacity: 0;} 
  to {opacity: 1;}
}

@keyframes fadeIn {
  from {opacity: 0;}
  to {opacity:1 ;}
}
</style>''')
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
print('''<div id="bg-image">''')
print('''<div id ="topnav">
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/show_applicant.py">Applicant List</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/applicant_stats.py">Applicant Statistics</a>
  <a  class = "active" href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/review_summary.py">My Past Reviews</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/help_reviewer.py">Help</a>
  <a  href="#contact">About/Contact</a>
  </div>''')

print("<h1> Review Summary</h1>")
		

#print("<h2>%s's Past Reviews </h2>" %(fname))
print('''<form name="ReviewForm" action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/review_summary.py" method="post" >
		<input type="hidden" id="id" name="uid" /><br>
		</form>''')
	
	
	
#must update to get hidden values ****
#get form values 
#form = cgi.FieldStorage()
uid = 2	
	
#create table
print("<table id=ReviewSummary>")
#create table headers
print('''<tr><th>Applicant Name</th><th>Review</th></tr>''')

#<th>Date Submitted</th>

form = cgi.FieldStorage()
uid = form.getvalue('uid')

#query to retrieve the user's id 
query1 = '''select firstname, lastname, reviews
			from Review join Applicant using(aid)'''
			#where uid = %s''' %uid	

connection = sqlite3.connect('db/BRITEREU.db')
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
	print('''<tr><td>%s %s</td><td>
			<div class="popop" onclick="myFunction()">
				<span class="popuptext" id="myPopup">%s</span>
			</div> 
			</td></tr>''' %(row[0], row[1], row[2]))

c.close()
connection.close()	

print("</table>")



print('''<script>
// When the user clicks on <div>, open the popup
function myFunction() {
  var popup = document.getElementById("myPopup");
  popup.classList.toggle("show");
}
</script>''')

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
            var tf = new TableFilter(ReviewSummary, filtersConfig);
            tf.init();
          </script>''')
          
#print('''
#<DIV id='PopUp' style='display: none; position: absolute; left: 100px; top: 100px; border: solid black 1px; padding: 10px; background-color: rgb(200,100,100); text-align: justify; font-size: 12px; width: 135px;' 
#onmouseclick="document.getElementById('PopUp').style.display = 'none' ">
#<SPAN id='PopUpText'>TEXT</SPAN>
#</DIV>>')

print("</body></html>")
