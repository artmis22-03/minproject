from flask import Blueprint, render_template,request
import mysql.connector

views=Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/signup', method=['GET','POST'])
def signup():
    


    return render_template("Signup.html")

@views.route('/authsignup',method=['GET','POST'])
def authsign():
    if request.method== 'POST':
        name=request.form.get['uname']
        email=request.form.get['email']
        password1=request.form.get['pass1']
        password2=request.form.get['pass2']
        c=mysql.connector.cursor()
        c.execute('select * from ')

@views.route('/check')
def lig():
    return render_template("abc.html")