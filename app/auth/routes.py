from flask import render_template
from . import auth
from .forms import RegisterForm, LoginForm


@auth.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('auth/register.html', form = form)


@auth.route('login')
def login_page():
    form = LoginForm()
    return render_template("auth/login.html", form = form)