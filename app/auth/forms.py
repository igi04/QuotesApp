import re
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import Length, EqualTo, Email, DataRequired
from app.models import User

class RegisterForm(FlaskForm):
    #My own validation methods
    def validate_password1(self, field):
        password = field.data
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError('The password should contain at least on special character')

    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError("Username already exists. Try a different username")

    def validate_email_address(self, field):
        email_address = User.query.filter_by(email=field.data).first()
        if email_address:
            raise ValidationError("E-mail address already exists. Try a different e-mail address")

    #Structure of register form
    username = StringField(label='Username',
                           validators=[Length(min=3, max=25, message='Username should be between 3-25 characters'),
                                       DataRequired()])
    email_address = StringField(label='E-mail',
                                validators=[Email(message="Incorrect e-mail form"), DataRequired()])
    password1 = PasswordField(label="Password",
                              validators=[Length(min=8, message='Password should be above 8 characters'),
                                          DataRequired()])
    password2 = PasswordField(label="Repeat Password",
                              validators=[EqualTo('password1', message="Passwords must be the same"), DataRequired()])
    submit = SubmitField(label='Create Account')


#Login form
class LoginForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label='Log in')
