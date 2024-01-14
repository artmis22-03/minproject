from flask import Blueprint, render_template,request
import mysql.connector

auth=Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    
    return render_template("Login.html")


@auth.route('/authenticate',methods=['GET','POST'])
def authent():
    if request.method== 'POST':
        email=request.form.get['email']
        password=request.form.get['password']
        
    cur=mysql.connector.cursor()
    # cur.execute("select * from users where password=%s",(password))
    
@auth.route('/authsignup',method=['GET','POST'])
def authsign():
    if request.method== 'POST':
        name=request.form.get['uname']
        email=request.form.get['email']
        password1=request.form.get['pass1']
        password2=request.form.get['pass2']
        c=mysql.connector.cursor()
        c.execute('select * from users where email=%s',(email))
        us=c.fetchone()
        if us:
            return render_template("abc.html")
        elif password1!=password2:
            return render_template("error.html")
        else:
            c.execute("insert into user values(%s,%s,%s)",(email,name,password1))
            return render_template("new.html")


