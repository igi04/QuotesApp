import re
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import Length, EqualTo, Email, DataRequired


def special_char_check(form, field):
    password = field.data
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValidationError('The password should contain at least on special character')


class RegisterForm(FlaskForm):
    username = StringField(label='Username',
                           validators=[Length(min=3, max=25, message='The username should be between 3-25 characters'),
                                       DataRequired()])
    email_address = StringField(label='E-mail',
                                validators=[Email(message="Incorrect e-mail form"), DataRequired()])
    password1 = PasswordField(label="Password",
                              validators=[Length(min=8, message='The password should be above 8 characters'),
                                          DataRequired(), special_char_check])
    password2 = PasswordField(label="Repeat Password",
                              validators=[EqualTo('password1', message="The passwords must be the same"), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label="Username")
    password = PasswordField(label="Password")
    submit = SubmitField(label='Login')
