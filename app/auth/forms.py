from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField(label='Username')
    email_address = StringField(label='E-mail')
    password1 = PasswordField(label="Password")
    password2 = PasswordField(label="Repeat Password")
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label="Username")
    password = PasswordField(label="Password")
    submit = SubmitField(label='Login')
