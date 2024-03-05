from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default = func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique= True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    title_URL = db.Column(db.String(255), nullable=True)
    image = db.Column(db.String(255), nullable=True)
    about_course = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    duration = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Float, nullable=True)
    instructors = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"Course('{self.title}', '{self.title_URL}', '{self.image}', '{self.about_course}', '{self.rating}', '{self.duration}', '{self.price}', '{self.instructors}')"