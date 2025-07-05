from flask_login import UserMixin
from sqlalchemy.orm import backref
from werkzeug.security import generate_password_hash

from app.extensions import db
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean

likes = db.Table('likes',
                 Column('user_id', Integer, ForeignKey('user.id')),
                 Column('quote_id', Integer, ForeignKey('quote.id'))
                 )


class User(UserMixin, db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(50), nullable=False)

    quotes = db.relationship('Quote', backref='author', lazy=True)
    liked_quotes = db.relationship('Quote', secondary=likes, backref=backref('liked_by', lazy='dynamic'),lazy='dynamic')


    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_password):
        self.password_hash = generate_password_hash(plain_password)

class Quote(db.Model):
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    author_name = Column(String(50), nullable=False)
    is_private = Column(Boolean, default=True)
    user_id = Column(db.Integer, ForeignKey('user.id'))
