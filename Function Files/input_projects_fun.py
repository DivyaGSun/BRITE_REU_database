import sys
import cgi
import cgitb
import sqlite3
reload(sys)
sys.setdefaultencoding('utf-8')
cgitb.enable()

def input_projects():
	# html
	print("Content-type: text/html\n")
	print('<meta charset="utf-8">')
	print("<html><head>")
	print("<title>BRITE REU Candidates</title>")
	print('''<style="white-space:pre-wrap; word-wrap:break-word">''')
	print('''<link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/nav.css">
         	<link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/project.css">
	</head>''')

	print("<body>")
	print('''<div id="bg-image">''')
	print('''<div id="topnav">
  	<a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/show_applicant_admin.py">Applicant List</a>
  	<a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/stats_admin.py">Applicant Statistics</a>
  	<a href="#assign users">Assign Users</a>
  	<a class="active" href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/input_projects.py">Input Faculty Projects</a>
  	<a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/review_summary_admin.py">View All Past Reviews</a>
  	<a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/assign_candidate.py">Assign Candidates to Faculty</a>
  	<a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/can_pref.py">Candidate Preferences</a>
  	<a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/match.py">Match Candidates to Faculty</a>
  	<a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/finalmatch.py">Final Matches</a>
  	<a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/help_admin.py">Help</a>
  	<a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/about_admin.py">About/Contact</a>
	</div>''')

	print("<h3>Enter Projects for Faculty Members in the Text Boxes | Click on ? for types of Filtering</h3>") 

	#query to get all faculty for the rows
	query1 = 'SELECT uid, fname || " " || lname FROM User WHERE role="faculty";'
	
	#query to get all projects currently in the Project table
	query2 = "SELECT uid, group_concat(project_name, '\n') FROM Project GROUP BY(uid);"
	
	
	#start connection
	connection = sqlite3.connect('db/BRITEREU.db')
	c = connection.cursor()
	try:
    		#execute query 1 
    		c.execute(query1)
    		#get results to above query
    		results1 = c.fetchall()
	except Exception:
    		print('<p><font color="red"><b>Error Query 1</b></font></p>')

	try:
    		#execute query 2 
    		c.execute(query2)
    		#get results to above query
    		results2 = c.fetchall()
	except Exception:
    		print('<p><font color="red"><b>Error Query 2</b></font></p>')

	c.close()
	connection.close()

	#retrieve form data
	form = cgi.FieldStorage()

	#check what textboxes are filled in and insert those project names into the Project table
	if form:
     		fprojects = []
     		for row in results1:
          		try:
               			if form.getvalue("%s" % row[0]) is not None:
                    			fprojects.append((row[0], form.getvalue("%s" % row[0])))
          		except Exception:
               			print("<p><font color=red><b>Error</b></font></p>")
     		connection = sqlite3.connect('db/BRITEREU.db')
     		c = connection.cursor()
     		for pair in fprojects:
          		insertStatement = 'INSERT INTO Project(uid, project_name) VALUES (%s, "%s");' % pair
          		c.execute(insertStatement)
          		connection.commit()
     		#checks if there is a project to be removed and if yes, deletes from the Project table
     		remove_proj = form.getlist("rproj")
     		for project in remove_proj:
          		deleteStatement = 'DELETE FROM Project WHERE project_name="%s" ;' % project
          		c.execute(deleteStatement)
          		connection.commit()
     		c.close()
     		connection.close()

	#query the database again to get all updated projects currently in the Project table
	query3 = "SELECT uid, group_concat(project_name, '\n') FROM Project GROUP BY(uid);"

	#start connection
	connection = sqlite3.connect('db/BRITEREU.db')
	c = connection.cursor()
	try:
    		#execute query 3 
    		c.execute(query3)
    		#get results to above standard query
    		results3 = c.fetchall()
	except Exception:
    		print('<p><font color="red"><b>Error Query 1</b></font></p>')


	#form for admin to type in projects for faculty members 
	print('''<form name="form" id="form" action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/input_projects.py" method="post" >''')
	print('<table id=Project class="dataframe">')
	print('''<tr><th>Faculty</th><th>Projects</th><th>Enter Project Name</th><th>Remove Project</th>''')

	#added proper URL for reference to reviewer page
	#print the faculty table with a textbox for each faculty member
	#add functionality to input projects currently in the database
	for row in results1:
    		for curr_proj in results3:
         		if curr_proj[0] == row[0]:
              			print('''<tr><td>%s</td><td>%s</td><td><input type="text" name=%s value="" /></td><td>''') % (row[1], (curr_proj[1]).replace("\n","<br/><br/>"), row[0])
              			tmp_proj = curr_proj[1].split("\n")
              			print('<select name="rproj"><option value="">-Select Project-</option>')
              			for proj_option in tmp_proj:
                   			print('<option value="%s">%s</option>') % (proj_option, proj_option)
              			print('</select></td></tr>')
              			break
    		else:
         		print('''<tr><td>%s</td><td> </td><td><input type="text" name=%s value="" /></td><td></td></tr>''') % (row[1], row[0]) 

	#add submit button for assigning faculty to candidates
	print('<input type="submit" value="Save Projects" /><br /><br />')

	#end form
	print("</form>")


	#filtering section for the table
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
            	var tf = new TableFilter(Project, filtersConfig);
            	tf.init();
          	</script>''')
	
	print("</body> </html>")
