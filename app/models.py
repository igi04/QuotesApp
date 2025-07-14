from flask_login import UserMixin
from sqlalchemy.orm import backref
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean, Time

#Likes helping table
likes = db.Table('likes',
                 Column('user_id', Integer, ForeignKey('user.id')),
                 Column('quote_id', Integer, ForeignKey('quote.id'))
                 )

#User table
class User(UserMixin, db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(50), nullable=False)
    daily_quote_enabled = Column(Boolean, default=False)
    daily_quote_time = Column(Time, default=None)
    daily_quote_category = Column(String(50), default=None)

    quotes = db.relationship('Quote', backref='author', lazy=True)
    liked_quotes = db.relationship('Quote', secondary=likes, backref=backref('liked_by', lazy='dynamic'),lazy='dynamic')

    #Work of hashing password
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_password):
        self.password_hash = generate_password_hash(plain_password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

#Quote table
class Quote(db.Model):
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    author_name = Column(String(50), nullable=False)
    category = Column(String(50), default="motivation")
    is_private = Column(Boolean, default=True)
    user_id = Column(db.Integer, ForeignKey('user.id'))
