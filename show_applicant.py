#!/usr/bin/python

#also I don't see any use of including cgi here because all this script is doing is showing data
import sys
import cgi
import cgitb
import sqlite3

cgitb.enable()

#start html
print("Content-type: text/html\n")
print("<html><head>")
print("<title>BRITE REU Applicants</title>")
print("<body>")
print("<h1>Applicant Information</h1>")

#did not include form action here in this script since user is not inputting anything yet

#start table
print("<table id=Applicant>")
#print headers for html table
print("<tr><th>Applicant ID</th><th>First Name</th><th>Last Name</th></tr>")

#query to print applicant data
query1 = "SELECT aid, firstname, lastname FROM Applicant;"

try:
    #connect to sqlite database file
    connection = sqlite3.connect('BRITEREU.db')
    c = connection.cursor()
    #execute query
    c.execute(query)
    #get results to above standard query
    results = c.fetchall()
    
    #print results of query to html table
    for row in results:
        print("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (row[0], row[1], row[2]))
    c.close()
    connection.close()

#query does not execute properly
except Exception:
    print("<p><font color=red><b>Error</b></p>")

print("</table>")
print("</body></html>")
