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

class HybridCar(db.Model):
    __tablename__ = 'hybridcar'
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(100))
    model = db.Column(db.String(100))
    year = db.Column(db.Integer)
    battery_capacity_kWh = db.Column(db.Float)
    fuel_efficiency_mpg = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  
    fuel_logs = db.relationship('FuelUsage', backref='car', lazy=True)  

class FuelUsage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fuel_used = db.Column(db.Float)
    distance_traveled = db.Column(db.Float)
    date = db.Column(db.DateTime(timezone=True), default=func.now)
    car_id = db.Column(db.Integer, db.ForeignKey('hybridcar.id'))  
#store videos
#class Reminder(db.model):