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
    


