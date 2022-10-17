from flask import Flask
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import os

file_db = create_engine("sqlite:///mydatabase.db")

def create_database():
    if (os.path.exists('mydatabase.db')):
        os.remove ('mydatabase.db')
    data = pd.read_csv("data.csv")
    newdata = data.head(15)    
    newdata.to_sql("bankInfo", file_db)
    return file_db

def create_app():
    
    file_db = create_database()

    app = Flask(__name__)

    from .views import views
    app.register_blueprint(views, url_prefix='/')
    
    return app 
    
   
    

