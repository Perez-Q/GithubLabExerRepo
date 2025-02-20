from Website import db, DB_NAME # from this package {website} import db.
from flask_login import UserMixin
from sqlalchemy.sql import func #Func is date and time

class Note(db.Model): # All notes looks like this 
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # ONE TO MANY


class User(db.Model, UserMixin): #This the schema User model
    id = db.Column(db.Integer, primary_key=True) #Make column of Int primary
    email = db.Column(db.String(150), unique=True) #Unique is well unique
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # stores all the notes of user owns/created

#store videos
#class Reminder(db.model):