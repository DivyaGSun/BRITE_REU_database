import sys
import cgi
import cgitb
import sqlite3
reload(sys)
sys.setdefaultencoding('utf-8')
cgitb.enable()

def show_applicant_admin():
	#begin html
	print("Content-type: text/html\n")
	print('<meta charset="utf-8">')
	print("<html><head>")
	print("<title>BRITE REU Applicants</title>")
	print('''<link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/nav.css">
                 <link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/appadmin.css">
	</head>''')

	#begin body of html
	#navigation bar and background design
	print("<body>")
	print('''<div id="bg-image">''')
	print('''<div id="topnav">
	<a class="active" href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/show_applicant_admin.py">Applicant List</a>
	<a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/stats_admin.py">Applicant Statistics</a>
	<a href="#assign users">Assign Users</a>
	<a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/input_projects.py">Input Faculty Projects</a>
	<a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/review_summary_admin.py">View All Past Reviews</a>
	<a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/assign_candidate.py">Assign Candidates to Faculty</a>
	<a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/can_pref.py">Candidate Preferences</a>
	<a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/match.py">Match Candidates to Faculty</a>
	<a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/finalmatch.py">Final Matches</a>
	<a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/help_admin.py">Help</a>
	<a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/about_admin.py">About/Contact</a>
	</div>''')


	print("<h1>Applicant Information</h1>")
	print("<h2>Selected Candidates</h2>")
	
	#retrieve Candidate form data to remove a candidate if there is any
	form = cgi.FieldStorage()
	
	#if form data was returned, remove the candidate from the Candidate table in the database
	if form:
		#get the list values from the many-value fields
		removelist = form.getlist("rcan")
		connection = sqlite3.connect('db/BRITEREU.db')
		c = connection.cursor()
		for candidate in removelist:
        		deleteStatement = "DELETE FROM Candidate WHERE cid = %d;" % int(candidate)
        		c.execute(deleteStatement)
        		connection.commit()
		c.close()
		connection.close()

	#retrieve Applicant form data to select a candidate if there is any
	form = cgi.FieldStorage()

	#if form data was returned, insert the applicant into the Candidate table
	if form:
		#get the list values from the many-value fields
		candidateslist = form.getlist("candidates")
		connection = sqlite3.connect('db/BRITEREU.db')
		c = connection.cursor()
		for candidate in candidateslist:
        		try:
        			insertStatement = "INSERT INTO Candidate(cid) VALUES (%d);" % int(candidate)
        			c.execute(insertStatement)
        			connection.commit()
        		except Exception:
        			pass
		c.close()
		connection.close()

	#Query 1 - get candidate information
	query_candidates = "SELECT cid, documents, firstname, lastname FROM Candidate join Applicant on Candidate.cid=Applicant.aid;"
	connection = sqlite3.connect('db/BRITEREU.db')
	c = connection.cursor()
	try:
		#execute query
		c.execute(query_candidates)
		#get results to above query
		results_candidates = c.fetchall()
	except Exception:
		print("<p><font color=red><b>Error Candidate Query</b></font></p>")

	#close connection to db file
	c.close()
	connection.close()

	#start Candidate form
	print('''<form name="form1" id="form1" action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/show_applicant_admin.py" method = "post">''')

	#print the candidate table headers
	print("<div>")
	print('<table id= Candidate class="dataframe">')
	print("<tr><th>Candidate ID</th><th>Full Application</th><th>First Name</th><th>Last Name</th><th>Remove Candidates</th></tr>")
	
	#print the candidate table
	for row in results_candidates:
		print('''<tr><td><a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/reviewer.py?AID=%s" target="_blank">%s</a></td><td>%s</td><td>%s</td><td>%s</td><td><input type="checkbox" name="rcan" value=%s /></td></tr</tr>''' % (row[0],row[0], row[1], row[2], row[3], row[0]))

	#add submit button for removing candidates
	print('<input type="submit" value="Remove Candidates" /><br /><br />')
	print("</table></div>")
	
	#end candidate form
	print("</form>")


	#Query 2 - get applicant information
	#Future Direction - make these fields dynamic so that the administrator can choose what fields to see
	query_applicants = "SELECT aid, documents, firstname || ' ' || lastname, country, firstgen, institution, standing, major, gpa, submitdate, reviewstatus FROM Applicant;"
	
	#start connection
	connection = sqlite3.connect('db/BRITEREU.db')
	c = connection.cursor()
	try:
		#execute query
		c.execute(query_applicants)
		#get results to above query
		results_applicants = c.fetchall()
	except Exception:
		print("<p><font color=red><b>Error Applicant Query</b></font></p>")

	#close connection to db file
	c.close()
	connection.close()


	#start Applicant form
	print('''<form name="form2" id="form2" action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/show_applicant_admin.py" method = "get">''')

	#print Applicant table and table headers
	print('<table id= Applicant class="dataframe">')
	print("<br /><br /><h2>Applicants</h2>")
	print("<h3>Select candidates by checking the checkboxes | Click on ? for types of Filtering</h3>")
	print("<tr><th>Select Candidates</th><th>Applicant ID</th><th>Full Application</th><th>Applicant Name</th><th>Country</th><th>First Gen</th><th>School</th><th>Standing</th><th>Major</th><th>GPA</th><th>Date Submitted</th><th>Review Status</th><th>Ranking</th></tr>")

	#print each row of the Applicant table and added proper URL for reference to reviewer page
	for row in results_applicants:
		print('''<tr><td><input type="checkbox" name="candidates" value=%s /></td><td><a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/reviewer.py?AID=%s" target="_blank">%s</a></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td></td></tr>''' % (row[0], row[0],row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],row[9], row[10]))

	#add submit button for selecting candidates
	print('<input type="submit" value="Submit Candidates" /><br /><br />')
	print("</table>")

	#end form
	print("</form>")


	#filtering for the Applicant table
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
	
