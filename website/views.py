from flask import Blueprint, render_template,request
import mysql.connector

views=Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/signup',methods=['GET','POST'])
def signup():
    return render_template("Signup.html")
