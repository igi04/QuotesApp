from flask import render_template, redirect, url_for, flash
from app.models import User
from app import db
from . import auth
from .forms import RegisterForm, LoginForm


@auth.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('main.home'))

    #If there are not errors from validations of the form
    if form.errors != {}:
        for err_message in form.errors.values():
            flash(err_message, category='danger')

    return render_template('auth/register.html', form = form)


@auth.route('login')
def login_page():
    form = LoginForm()
    return render_template("auth/login.html", form = form)