from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os 

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db = SQLAlchemy(app)
    return(app)