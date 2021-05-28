import sys
import cgi
import cgitb
import sqlite3
reload(sys)
#import sys
sys.setdefaultencoding('utf-8')

cgitb.enable()

def show_login():
    print("Content-type: text/html\n")
    print('<meta charset="utf-8">')
    print('<meta name="viewport" content="width=device-width, initial-scale=1">')
    print("<html><head>")

    print('''

    <link rel="stylesheet" href="https://bioed.bu.edu/students_21/group_proj/group_K/css/login.css">''')

    print('''<style>

    #my_form p:nth-child(3){
        float: left !important;
        width: 50% !important;
    }
    #my_form p:nth-child(4) {
        float: right !important;
        width: 50% !important;
    }


    </style>

    </head>''')


    print("<body>")
    print('''<form id="my_form" form action="https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/login.py"  onsubmit ="return checklogin();" method="POST">
        <p class="clearfix">
            <label for="login">Email</label>
            <input type="text" name="login" id="login" placeholder="Email">
        </p>
        <p class="clearfix">
            <label for="password">Password</label>
            <input type="password" name="password" id="password" placeholder="Password">
        </p>
        <p class="clearfix">
            <input type="submit" name="submit" value="Sign in">
        </p>
        <p class="clearfix">
            <input type="button" value="Create Account" onclick = "location.href='https://bioed.bu.edu/cgi-bin/students_21/group_proj/group_K/create_account.py'">
        </p>
    </form>''')


    def verify_password(stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password


    form = cgi.FieldStorage()
    Username = form.getvalue('login')
    password = form.getvalue('password')

    if Username and password:
        Query1 = '''Select exists (SELECT username FROM User WHERE username='%s')''' %Username
        connection = sqlite3.connect('db/BRITEREU.db')
        c = connection.cursor()
        try:
            c.execute(Query1)
            exists = [x[0] for x in c.fetchall()][0]

        except Exception:
            print(str(exists))
            print("<p><font> color=red><b>Error Q1</b></font></p>")
        if exists:
            Query2 = '''select password from User where username='%s' ''' %Username
            try:
                c.execute(Query2)
                old_pass = str([x[0] for x in c.fetchall()][0])
                exists_pass= str(verify_password(old_pass, password))
            except Exception:
                print("<p><font> color=red><b>Error Q2</b></font></p>")
            if exists_pass:
                Query3 = '''select role from User where username='%s' ''' %Username
                try:
                    c.execute(Query3)
                    role = str([x[0] for x in c.fetchall()][0])
                except Exception:
                    print("<p><font> color=red><b>Error Q3</b></font></p>")
                if role:
                    Query4 = '''select uid from User where username='%s' ''' %Username
                    try:
                        c.execute(Query4)
                        uid = [x[0] for x in c.fetchall()][0]
                    except Exception:
                        print("<p><font> color=red><b>Error Q3</b></font></p>")

            c.close()
            connection.close()

        if exists and exists_pass:
            print(exists, exists_pass, role, uid)
            #becomes undefined because of reload;
    #         print('''<script type="text/javascript">
    #
    #         function checklogin()  {
    #             var user_exists = int(%s)
    #             var pass_match = string(%s)
    #             var roles = string(%s)
    #             $ajax
    #             if (user_exists == 0) {
    #                 alert ("Username not found")
    #                 return false;
    #             }
    #             else if (pass_match == "False") {
    #                 alert ("password doesn't match username try again")
    #                 return false;
    #             }
    #
    #             // If same return True.
    #             if (role == 'Reviewer') {
    #                     alert ('u')
    #                     window.location.href = "www.youtube.com";
    #             }
    #             else if (role == 'Faculty') {
    #                     window.location.href = "www.google.com"
    #             }
    #         }
    #         </script>''' %(exists, exists_pass, role))
    # )




    print("</body></html>")
