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

print('''<html><head>
<title>Applicant Statistics</title>
<link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/nav.css">

<style>
body {margin:30;padding:30;}
</style></head>''')

print('''<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<body>
<div id="bg-image">
<div id ="topnav">
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/show_applicant_admin.py">Applicant List</a>
  <a  class="active" href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/stats_admin.py">Applicant Statistics</a>
  <a  href=""> Assign Users</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/input_projects.py">Input Faculty Projects</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/review_summary_admin.py">View All Past Reviews</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/assign_candidate.py">Assign Candidates to Faculty</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/can_pref.py">Candidate Preferences</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/match.py">Match Candidates to Faculty</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/finalmatch.py">Final Matches</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/help_admin.py">Help</a>
  <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/about_admin.py">About/Contact</a>
  </div>''')

print(''' 
<h1>Applicant Statistics Page</h1>
<h4>Below shows various pie chart graphs to visualize the applicant's data. These graphs include the applicant's genders, expected graduate school years, and the percentage of first-generation applicants. </h4>

<div id="piechart" style="width: 50%; float: left;"></div>
<div id="piechart2" style="margin-left: 50%;"></div>
<div id="piechart3"></div>

</body>

<script type="text/javascript">
// Load google charts
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

// Draw the chart and set the chart values
function drawChart() {
  var data = google.visualization.arrayToDataTable([
  ['Gender', 'Numbers of Students'],
  ['Female', 141],
  ['Male', 92],
  ['Non-bindary', 4]
]);

  // Optional; add a title and set the width and height of the chart
  var options = {'title':'Genders', 'width':550, 'height':400};

  // Display the chart inside the <div> element with id="piechart"
  var chart = new google.visualization.PieChart(document.getElementById('piechart'));
  chart.draw(data, options);
}
</script>
<script type="text/javascript">
// Load google charts
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

// Draw the chart and set the chart values
function drawChart() {
  var data = google.visualization.arrayToDataTable([
  ['Year Entering Grad School', 'School Year'],
  ['2022', 102],
  ['2023', 111],
  ['No current plan', 24]
]);

  // Optional; add a title and set the width and height of the chart
  var options = {'title':'Expected to Enter Grad School', 'width':550, 'height':400};

  // Display the chart inside the <div> element with id="piechart"
  var chart = new google.visualization.PieChart(document.getElementById('piechart2'));
  chart.draw(data, options);
}
</script>
<script type="text/javascript">
// Load google charts
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

// Draw the chart and set the chart values
function drawChart() {
  var data = google.visualization.arrayToDataTable([
  ['First Generation Students', 'Numbers of Students'],
  ['Yes', 54],
  ['No', 183],
]);

  // Optional; add a title and set the width and height of the chart
  var options = {'title':'First Generation Students', 'width':550, 'height':400};

  // Display the chart inside the <div> element with id="piechart"
  var chart = new google.visualization.PieChart(document.getElementById('piechart3'));
  chart.draw(data, options);
}
</script>

</html>''')
