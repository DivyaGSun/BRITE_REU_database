import sys
import cgi
import cgitb
import sqlite3
reload(sys)
sys.setdefaultencoding('utf-8')
cgitb.enable()

# html
print("Content-type: text/html\n")
print('<meta charset="utf-8">')
print("<html><head>")
print('''<link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/nav.css">''')
print('''<style>
body {margin:30;padding:30;}
</style> </head>''')
print("<title>Admin Help Page</title>")
print('''</head>''')

print("<body>")
print('''<div id="bg-image">''')
print('''<div id ="topnav">
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/show_applicant_admin.py">Applicant List</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/stats_admin.py">Applicant Statistics</a>
  <a  href="#Assign Users">Assign Users</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/input_projects.py">Input Faculty Projects</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/review_summary_admin.py">View All Past Reviews</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/assign_candidate.py">Assign Candidates to Faculty</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/can_pref.py">Candidate Preferences</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/match.py">Match Candidates to Faculty</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/finalmatch.py">Final Matches</a>
  <a  class ="active" href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/help_admin.py">Help</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/about_admin.py">About/Contact</a>
  </div>''')
  
print('''<h1>Admin: Help Page</h1>
<h2>For help using webpages see below:</h2>
<h3>Applicant List: </h3>
<p>
- The bottom table under "Applicants" shows all the applicants and their information. <br />
- To filter through the table, search in the top search boxes on the table. <br />
- To see the review page for an applicant, click on the hyperlinked applicant ID number on the left side of the table. <br />
- To select a candidate, check the checkbox on the right side of the Applicant table under "Select Candidates" and click "Submit Candidates" <br />
- The selected candidates will show up in the above table under "Selected Candidates". <br />
- To remove a candidate, check the checkbox on the right side of the Candidate table under "Remove Candidates" and click "Remove Candidates" <br />
</p>

<p>
- After clicking on the applicant ID hyperlink, this will lead you to the review page for the applicant. <br />
- A review can be written in the text box provided. <br />
- After clicking "Submit", the review will be recorded. <br />
- On the right hand side, all previous reviews recorded for this applicant are shown. <br />
- At the bottom of the page, you can click "Back to Applicant Page" to return to the main applicant table. 
</p>

<h3>Applicant Statistics: </h3>
<p>
- This page displays information about the makeup of the applicant pool. </p>

<h3>Assign Users: </h3>
<p>Add assign users info </p>

<h3>Input Faculty Projects </h3>
<p>
- The faculty names are shown on the left side of the table. <br />
- If there is a project currently in the database for that faculty member, it will be shown in the second column under "Projects" <br />
- Enter a project name for a faculty member in the corresponding text box under "Enter Project Name" <br />
- If you would like to remove a project, select a project from the dropdown for the corresponding faculty member under "Remove Project" <br />
- Click "Submit Projects" to save your changes. 
</p>

<h3>Assign Candidates to Faculty: </h3>
<p>
- Candidate IDs and Names are shown on the left side of table. <br />
- Faculty with projects currently stored in the database will show up as columns in the table header. <br />
- When the page loads, all currently assigned pairs stored in the database will be checked. <br />
- The timestamp of the assignment can be seen by hovering over the checked checkbox. Time is in GMT timezone. <br />
- If you would like to select an additional assignment, check the unchecked box. <br />
- If you would like to remove a current assignment, uncheck the checked box. <br />
- Click "Assign Candidates" to save your changes. <br />
- Now, when the page loads, it will show all assignments currently in the database and include changes that were just made. <br /> 
</p>

<h3>Candidate Preferences: </h3>
<p>
- Using the drop downs, select the name of the candidate and their top choices of projects, up to 5. <br />
- Preferences for candidates can also be removed by selecting a checkbox next to one fo the candidate's preferences and selecting the "Remove rankings" button.  <br />

</p>

<h3>Match Candidates to Faculty: </h3>
<p>
- Candidate IDs and Names are shown on the left side of table. <br />
- Faculty with projects currently stored in the database will show up as columns in the table header. <br />
- When the page loads, all currently assigned pairs stored in the database will be checked. <br />
- Candidate rankings of projects, as well as the faculty ranking of that candidate appear in a table at the bottom of the page.<br />
- If you would like to add a match, select any uncheckked checkbox. <br />
- if you would like to remove a match, select any checked checkbox. <br />
- Click "Make Matches" to update the final matched pairs. <br />

</p>

<h3>Final Matches: </h3>
<p>
- View all final matched faculty and candidate pairs. <br />
- Faculty will have a filtered version of this page to view their final assigned candidates. <br />

</p>

<h3>Please Note: </h3>
<p>
Current Role: Admin </p></body>''')
print("</html>")
