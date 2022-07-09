from sqlalchemy import BigInteger, String, Column
from db_config import Base
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, Response, redirect, render_template, url_for, jsonify, make_response


app = Flask(__name__)
db = SQLAlchemy(app)

# Database ORMs
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(80))