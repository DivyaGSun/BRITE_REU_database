import sys
import cgi
import cgitb
import sqlite3
reload(sys)
#import sys
sys.setdefaultencoding('utf-8')

cgitb.enable()

def show_create():
    print("Content-type: text/html\n")
    print('<meta charset="utf-8">')
    print('<meta name="viewport" content="width=device-width, initial-scale=1">')
    print("<html><head>")

    print('''

    <link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/login.css">

    </head>''')

    print("<body>")
    print('''<div id="bg-image">''')
    print('''
    <form id="my_form" form action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/create_account.py" onsubmit = "return checkPassword();" method="POST">
        <p style = "text-align: center; Color:white;"><b>Please capitalize the first letter of your first and last name</b></p>
        <p class="clearfix">
            <label for="your_fname">First Name</label>
            <input type="text" name="your_fname" id="fname" placeholder="First Name" required>
        </p>
        <p class="clearfix">
            <label for="your_lname">Last Name</label>
            <input type="text" name="your_lname" id="lname" placeholder="Last Name" required>
        </p>
        <p style = "text-align: center; Color:white;"><i>Please enter Faculty or Reviewer</i></p>
        <p class="clearfix">
            <label for="your_role">Role</label>
            <input type="text" name="your_role" id="role" placeholder="Role" required>
        </p>
        <p class="clearfix">
            <label for="login">Email</label>
            <input type="text" name="login" id="login" placeholder="email"required>
        </p>
        <p class="clearfix">
            <label for="password">Password</label>
            <input type="password" name="password" id="password" placeholder="Password" required>
        </p>
        <p class="clearfix">
            <label for="psw-repeat">Repeat Password</label>
            <input type="password" name= "re_pass" id= "rpt_pass" placeholder="Repeat Password" required>
        </p>
        <p class="clearfix">
            <input type="submit" name="submit" value="Submit">
        </p>
        <p class="clearfix">
            <input type="button" value="Sign-in" onclick = "location.href='https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/login.py'">
        </p>
    </form>

    ''')


    print('''<script type="text/javascript">

    // Function to check Whether both passwords
    // is same or not.
    function checkPassword()  {
        var password1 = document.getElementById("password").value;
        var password2 = document.getElementById("rpt_pass").value;
        var roles = document.getElementById("role").value;
        // If Not same return False.
        if (password1 != password2) {
            alert ("Password did not match: Please try again")
            return false;
        }
        else if (roles != "Reviewer" && roles != "Faculty") {
            alert ("Role must be Faculty or Reviewer with proper capitalization")
            return false;
        }

        // If same return True.
        else{
            alert ("Account Created")
            return true;
        }
    }
    </script>''')
    #get form VALUES
    form = cgi.FieldStorage()
    # get three values from the form
    fname = form.getvalue('your_fname')
    lname = form.getvalue('your_lname')
    role = form.getvalue('your_role')
    Username = form.getvalue('login')
    password = form.getvalue('password')

    def hash_password(password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                    salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    if password:
        hash_pass = hash_password(password)
        insert = "INSERT INTO User (lname, fname, username, password, role) VALUES (?,?,?,?,?)"

    #connection = sqlite3.connect('/https://bioed.bu.edu/students_21/divyas3/BRITEREU.db')
        connection = sqlite3.connect('db/BRITEREU.db')
        c = connection.cursor()

        try:
            c.execute(insert, (lname, fname, Username, hash_pass, role))
            connection.commit()


        except Exception:
            print("<p><font> color=red><b>Error</b></font></p>")

        c.close()
        connection.close()

    print("</body></html>")
