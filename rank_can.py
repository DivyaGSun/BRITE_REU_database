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
print("<title>Faculty Ranking Candidates</title>")
print('''<style>
body {margin:30;padding:30;}
h1 {
  font-size: 30px;
  color: #000;
  border-bottom: 2px solid #ccc;
  padding-bottom: 5px;
}
#RankCandidate {
        font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
        border-collapse: collapse;
        width: 50%;
}
#RankCandidate td, #Applicant th {
        border: 1px solid #ddd;
        padding: 8px;
}
#RankCandidate tr:nth-child(even){background-color: #f2f2f2;}
#RankCandidate tr:hover {background-color: #ddd;}
#RankCandidate th {
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: left;
        background-color: #5C30B2;
        color: white;
}
</style>
</head>''')

print("<body>")
print("<h1>Rank Candidates</h1>")
print("<h2>Please rank your preferred candidates: 1 being the highest, 3 being the lowest</h2>")

#print('''<table id=RankCandidate>''')

#add radio button style options, for top five candidates 
print("<form name='Ranking' action='Submit' method='post'/>")
print('''Candidate 1: <input type="radio" name="rank" value="rank 1" /> 1 
		<input type="radio" name="rank" value="rank 2" /> 2
		<input type="radio" name="rank" value="rank 3" /> 3 
		<input type="radio" name="rank" value="rank 4" /> 4
		<input type="radio" name="rank" value="rank 5" /> 5 <br />
		Candidate 2: <input type="radio" name="rank2" value="rank 1" /> 1 
		<input type="radio" name="rank2" value="rank 2" /> 2
		<input type="radio" name="rank2" value="rank 3" /> 3 
		<input type="radio" name="rank2" value="rank 4" /> 4
		<input type="radio" name="rank2" value="rank 5" /> 5 <br />
		Candidate 3: <input type="radio" name="rank3" value="rank 1" /> 1 
		<input type="radio" name="rank3" value="rank 2" /> 2
		<input type="radio" name="rank3" value="rank 3" /> 3 
		<input type="radio" name="rank3" value="rank 4" /> 4
		<input type="radio" name="rank3" value="rank 5" /> 5 <br />
		Candidate 4: <input type="radio" name="rank4" value="rank 1" /> 1 
		<input type="radio" name="rank4" value="rank 2" /> 2
		<input type="radio" name="rank4" value="rank 3" /> 3 
		<input type="radio" name="rank4" value="rank 4" /> 4
		<input type="radio" name="rank4" value="rank 5" /> 5 <br />
		Candidate 5: <input type="radio" name="rank5" value="rank 1" /> 1 
		<input type="radio" name="rank5" value="rank 2" /> 2
		<input type="radio" name="rank5" value="rank 3" /> 3 
		<input type="radio" name="rank5" value="rank 4" /> 4
		<input type="radio" name="rank5" value="rank 5" /> 5 <br />
		<input type="submit" value="submit" />
		</form>''')

#testing document viewing link 	
print('''<p><a href="https://docs.google.com/document/d/1YLan2t1UVf-Pi7aEfdaWu9mV3sxvd6ndSZGR-y-hH8w/edit">View Candidate 1's Application</a></p>''')
print('''<p><a href="https://docs.google.com/document/d/1YLan2t1UVf-Pi7aEfdaWu9mV3sxvd6ndSZGR-y-hH8w/edit">View Candidate 2's Application</a></p>''')
print('''<p><a href="https://docs.google.com/document/d/1YLan2t1UVf-Pi7aEfdaWu9mV3sxvd6ndSZGR-y-hH8w/edit">View Candidate 3's Application</a></p>''')
print('''<p><a href="https://docs.google.com/document/d/1YLan2t1UVf-Pi7aEfdaWu9mV3sxvd6ndSZGR-y-hH8w/edit">View Candidate 4's Application</a></p>''')
print('''<p><a href="https://docs.google.com/document/d/1YLan2t1UVf-Pi7aEfdaWu9mV3sxvd6ndSZGR-y-hH8w/edit">View Candidate 5's Application</a></p>''')




connection = sqlite3.connect('BRITEREU.db')
c = connection.cursor()

#get uid hidden value from login 
uid = 	
query = '''SELECT cid
		from Assignment
		where uid = %s''' %uid
		
		
c.execute(query1)
results = c.fetchall()
for row in results:
	print('''<form>%s</form>''' %(row[0]))


print("</body></html>")



#NEED TO UPDATE: 
#get candidates from assigned candidate to faculty page
#get application from applicant table 
#create submission view update 