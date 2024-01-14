from flask import Blueprint, render_template,request
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="harsha",
  database="qwerty"
)
auth=Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    
    return render_template("Login.html")


@auth.route('/authenticate',methods=['GET','POST'])
def authent():
    if request.method== 'POST':
        email=request.form.get('email')
        password=request.form.get('password')
        
    cur=mydb.cursor()
    cur.execute("select * from users where email=%s",(email,))
    c=cur.fetchone()
    if c:
        return render_template("new.html")
    else:
        return render_template("error.html")

    



    
@auth.route('/authsignup',methods=['GET','POST'])
def authsign():
    if request.method == 'POST':
        name = request.form.get('uname')
        email = request.form.get('email')
        password1 = request.form.get('pass1')
        password2 = request.form.get('pass2')
        
        c = mydb.cursor()
        c.execute('SELECT * FROM users WHERE email=%s', (email,))
        us = c.fetchone()

        if us:
            return render_template("abc.html")
        elif password1 != password2:
            return render_template("error.html")
        else:
            # Use placeholders in the INSERT statement to prevent SQL injection
            c.execute("INSERT INTO users (email, name, password) VALUES (%s, %s, %s)", (email, name, password1))
            mydb.commit()
            return render_template("new.html")
# def authsign():
#     if request.method== 'POST':
#         name=request.form.get['uname']
#         email=request.form.get['email']
#         password1=request.form.get['pass1']
#         password2=request.form.get['pass2']
#         c=mydb.cursor()
#         c.execute('select * from users where email=%s',(email))
#         us=c.fetchone()
#         if us:
#             return render_template("abc.html")
#         elif password1!=password2:
#             return render_template("error.html")
#         else:
#             c.execute("insert into users values("+email+","+name+","+password1+")")
#             mydb.commit()
#             return render_template("new.html")


