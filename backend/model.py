from flask import Flask, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class Upload(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     filename = db.Column(db.String(100), nullable=False)
#     data = db.Column(db.LargeBinary)

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    fp = db.Column(db.String(264), unique=True)

    def __repr__(self):
        return f"Upload: {self.filename}"

    def __init__(self, filename, fp):
        self.filename = filename
        self.fp = fp