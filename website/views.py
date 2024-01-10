from flask import Blueprint, render_template

views=Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/signup')
def login():
    return render_template("Signup.html")

@views.route('/check')
def lig():
    return render_template("abc.html")