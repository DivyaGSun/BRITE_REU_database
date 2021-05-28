import sys
import cgi
import cgitb
import sqlite3
reload(sys)
#import sys
sys.setdefaultencoding('utf-8')

cgitb.enable()

def show_about_R():
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
      <a  href= "https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/main.py?t_ID=7">Help</a>
      <a  class = "active" href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/main.py?t_ID=8">About/Contact</a>
      </div>''')

    print('''<h3>About: </h3>
    <p>The BRITE REU Program, Bioinformatics Research and Interdisciplinary Training Experience, is an NSF funded summer mentored research program for undergraduate students who work full time in a lab for ten weeks and participate in various training activities.
    The BRITE REU database is used to store all the applicant data. This website acts as a portal to the database information.
    This website allows applicants to be easily reviewed. This website also helps the admin to assign candidates to faculty projects. </p>
    <p> This database and website were created by Boston University Bioinformatics graduate students.
    This project was developed as apart of their coursework for BF768 in the Spring of 2021.
    The project was completed under the supervision of Gary Benson. </p>
    <h3>Contact Information: </h3>
    <p>Gary Benson: gbenson@bu.edu <br />
    Divya Sundaresan: divyas3@bu.edu <br />
    Marissa Chiaradio: mdc98@bu.edu <br />
    Kenzie Knox: mfknox@bu.edu <br />
    Janvee Patel: jpatel2@bu.edu </p></body>''')
    print("</html>")
