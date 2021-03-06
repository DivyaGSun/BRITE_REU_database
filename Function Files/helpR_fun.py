import sys
import cgi
import cgitb
import sqlite3
reload(sys)
#import sys
sys.setdefaultencoding('utf-8')

cgitb.enable()

def show_help_R():
    print("Content-type: text/html\n")
    print('<meta charset="utf-8">')
    print("<html><head>")
    print('''<link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/nav.css">''')
    print('''<style>
    body {margin:30;padding:30;}
    </style> </head>''')
    print("<title>Reviewer Help Page</title>")
    print('''</head>''')

    print("<body>")
    print('''<div id="bg-image">''')
    print('''<div id ="topnav">
      <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/main.py?t_ID=3">Applicant List</a>
      <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/main.py?t_ID=5">Applicant Statistics</a>
      <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/main.py?t_ID=6">My Past Reviews</a>
      <a  class = "active" href= "https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/main.py?t_ID=7">Help</a>
      <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/main.py?t_ID=8">About/Contact</a>
      </div>''')

    print('''<h1>Reviewer: Help Page</h1>
    <h2>For help using webpages see below:</h2>
    <h3>Applicant List: </h3>
    <p>This page shows a table of all the applicants and their information. <br />
    To filter through the table, search in the top search boxes on the table <br />
    To write a review, please click on the hyperlinked applicant ID number on the left side of the table.
    </p>
    <h3>Submit A Review: </h3>
    <p>After clicking on the applicant ID hyperlink this will lead you to the submit a review page. <br />
    You may enter your review in the text box provided. <br />
    After clicking submit, your review will be recorded. <br />
    On the right hand side, you are able to see all the previous reviews recorded for this applicant. <br />
    At the bottom of the page, you make click "Back to Applicant Page" to return to the main applicant table.
    </p>
    <h3>Applicant Statistics: </h3>
    <p>This page hosts various graphs to visualize data about our applicants. <br />
    This page is for viewing purposes only right now.
    </p>
    <h3>My Past Reviews: </h3>
    <p>This page is the review summary page. <br />
    Here you will be able to view a table of all your previously submitted reviews. <br />
    You have the option to edit past reviews: by clicking on the review, making your edits, and clicking the save button.
    </p>
    <h3>Please Note: </h3>
    <p>Depending on your login role, you will only have access to certain pages. <br />
    If you are struggling to gain correct access please contact the admin: Gary Benson, gbenson@bu.edu. <br />
    </p>
    <h4>Current Role: Reviewer </h4></body>''')
    print("</html>")
