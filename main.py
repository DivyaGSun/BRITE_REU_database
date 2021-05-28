#!/usr/bin/python
#!/anaconda3/bin/python
##!/usr/local/Python-3.7/bin/python

import sys
import cgi
import cgitb
import sqlite3
#reload(sys)

#define file paths (import os) os.path.join

#import login/create Account
#from login_fun.py import show_login
#from create_acc_fun.py import show_create

#import reviewer files
from show_app_fun import show_applicant
from show_reviewer_fun import show_reviewer
from stats_fun import show_stats
from rev_summary_fun import show_past_revs
from helpR_fun import show_help_R
from aboutR_fun import show_about_R

#import admin files
from show_applicant_admin_fun import show_applicant_admin
#assign users file
from input_projects_fun import input_projects
#view all past reviews file
from assign_candidate_fun import assign_candidates
#candidate preferences file
#match candidates to faculty file
#final matches file
#from helpA_fun import show_help_A

#import faculty files

cgitb.enable()

form = cgi.FieldStorage()

if form:
    task_id = form.getvalue('t_ID')
    if task_id:
        # if task_id == "1":
        #     show_login()
        # if task_id == "2":
        #     show_create()
        #REVIEWERS
        if task_id == "3":
            show_applicant()
        if task_id == "4":
            show_reviewer()
        if task_id == "5":
            show_stats()  #stats page for all roles
        if task_id == "6":
            show_past_revs()
        if task_id == "7":
            show_help_R()
        if task_id== "8":
            show_about_R() #about page for all roles
        #ADMIN
        if task_id == "9":
            show_applicant_admin()
        #if task_id == "10":
            #assign users
        if task_id == "11":
            input_projects()
        if task_id == "12":
            assign_candidates()
        #if task_id == "13":
            #candidate pref
        #if task_id == "14":
            #match candidates to faculty
        #if task_id == "15":
            #final matches
        #if task_id == "16":
            #show_help_A()
        #FACULTY


# print("Content-type: text/html\n")
# print('<meta charset="utf-8">')
# print("<html><head>")
# print("<h1>BRITE REU Applicants</h1>")
# print("<p><font> color=red><b>Error</b></font></p>")
print("</head></html>")
