#!/usr/bin/python
import sys
import cgi
import cgitb
import sqlite3
reload(sys)
#import sys
sys.setdefaultencoding('utf-8')

cgitb.enable()

def show_reviewer():
    print("Content-type: text/html\n")
    print('<meta charset="utf-8">')
    print("<html><head>")
    print('''

    <link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/nav.css">
    <link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/reviewer.css">


    </head>''')



    print("<body>")
    form = cgi.FieldStorage()
    # get three values from the form
    t_ID = str(form.getvalue('t_ID'))
    AID = str(form.getvalue('AID'))
    Rev = form.getvalue('Review')
    UID = str(0)

    print('''<div id="bg-image">''')

    print('''<div id ="topnav">
      <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/main.py?t_ID=3">Applicant List</a>
      <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/main.py?t_ID=5">Applicant Statistics</a>
      <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/main.py?t_ID=6">My Past Reviews</a>
      <a  href= "https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/main.py?t_ID=7">Help</a>
      <a  href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/main.py?t_ID=8">About/Contact</a>

    </div>''')
    print("<h1>Submit a Review</h1>")


    print('''<form name="myForm" form action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/main.py" method="GET" >
            <input type ='hidden' id='t_ID' name="t_ID" value = %s>
            <input type ='hidden' id='ID' name="AID" value = %s>

            <label for="Review"><br>Enter review of Applicant:</label>
            <textarea id="Review" name="Review" rows="20" cols="80" placeholder = "Lorem ipsum dolor sit amet, te his apeirian complectitur. Ea sed prompta lobortis, eum id habemus periculis neglegentur, est eius quas placerat id. Ea duo dicit impetus oblique, dolor consul verear in vix. Ex quo cibo vitae fabulas. Ex vel meis omittantur, an modo wisi ius. Pro erat aliquando conceptam ea. Duo reque scaevola argumentum ea, dicat omittam an nec, in cibo numquam elaboraret eum. Quis voluptaria argumentum has ut." ></textarea>
            <input type="submit" onclick= "clicked()" value="Submit">
    		</form>'''%(t_ID, AID))

    # AID = str(form.getvalue('AID'))
    # Rev = str(form.getvalue('Review'))
    # UID = str(0)
    # AIDs = str(AID)

    query1 = """SELECT aid, firstname, lastname, emailaddress, submitdate, reviewstatus
    FROM Applicant
    WHERE aid='%s';""" %(AID)

    query2 = """SELECT created_at, reviews
    FROM Review
    WHERE aid='%s' and uid = '%s'
    order by created_at Desc;""" %(AID, UID)

    #connection = sqlite3.connect('/https://bioed.bu.edu/students_21/divyas3/BRITEREU.db')
    connection = sqlite3.connect('db/BRITEREU.db')
    c = connection.cursor()
    try:
        #execute query
        c.execute(query1)
        #get results to above standard query
        results = c.fetchall()
        #execute query
        c.execute(query2)
        #get results to above standard query
        past_reviews = c.fetchall()


    except Exception:
        print("<p><font> color=red><b>Error</b></font></p>")


    print("<h3>Applicant Information</h3>")
    print("<table id=Applicant>")
    print("<tr><th>Applicant ID</th><th>First Name</th><th>Last Name</th><th>Email Address</th><th>Date Submitted</th><th>Review Status</th></tr>")

    for row in results:
        print('''<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>''' % (row[0], row[1], row[2], row[3], row[4], row[5]))

    print("</table>")

    if Rev:
        insert = "INSERT INTO Review (aid,uid,reviews) VALUES (?,?,?)"
        update = '''UPDATE Applicant set reviewstatus = 'Completed' WHERE aid='%s';''' %(AID)
        try:
            c.execute(insert, (AID, UID , Rev))
            c.execute(update)
            connection.commit()
        #except Exception as sqlError:
           # print(sqlError)
    	#print(str(AID))
            #print(str(UID))
            #print("|%s|"%(Rev))
        except sqlite3.Error as er:
        	print('SQLite error: %s' % (' '.join(er.args)))
        	print("Exception class is: ", er.__class__)
        	print('SQLite traceback: ')
        	exc_type, exc_value, exc_tb = sys.exc_info()
        	print(traceback.format_exception(exc_type, exc_value, exc_tb))
            # print(str(AID))
            # print(str(UID))
            # print("|%s|"%(Rev))
        # prnt("<h2>Thanks your Review for Applicant Id %s have been recorded!</h2>" %AIDs)
        # query2 = "UPDATE Applicant set reviewstatus = Completed"
        # c.execute(query)


    c.close()
    connection.close()
    #print("</table>")

    print('Link to download full application:---(hyperlink this)')

    print('''<br><br><br><a href="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/show_applicant.py" class="button">Back to Applicant Page </a>''')

    items =[]
    for row in past_reviews:
        items.append(row)
    items = [list(ele) for ele in items]
    print('''<div id="past_rev">
          <h3>Previous Reviews Completed</h3>
          <p><i>If other reviews for this applicant have been completed by you they will be listed here </i></p>
          <table id = Review>''')
    for i in items:
        print ('<tr>')
        print ('<td>'+i[0]+'</td><td>'+i[1]+'</td>')
        print('</tr>')
    print('''</table>
          </div>''')


    print('''<script type="text/javascript">
        function clicked() {
           if (confirm('Do you want to submit?')) {
               submit.submit();
           } else {
               return false;
           }
        }



    </script>''')
    print("</body></html>")
