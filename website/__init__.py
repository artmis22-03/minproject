from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import mysql.connector 






db=SQLAlchemy()
db_name="database.db"

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="harsha",
  database="qwerty"
)

cu=mydb.cursor()

cu.execute("CREATE TABLE IF NOT EXISTS users(slno integer(5),name varchar(20),password varchar(20))")


def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='qwdfghjihgfd'
    #using sqlite for the database
    #app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{db_name}'
    #using mysql as the database
    app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:harsha@localhost/qwerty'
    db.init_app(app)

    from .views import views
    from .auth import auth
    #from .models import models

    

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')



    return app

