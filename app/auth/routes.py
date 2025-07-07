from flask import render_template, redirect, url_for, flash
from app.models import User
from app import db
from . import auth
from .forms import RegisterForm, LoginForm
from flask_login import login_user, login_required, logout_user


@auth.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        flash(["You created the account successfully"], category='success')
        return redirect(url_for('auth.login_page'))

    #If there are not errors from validations of the form
    if form.errors != {}:
        for err_message in form.errors.values():
            flash(err_message, category='danger')

    return render_template('auth/register.html', form = form)


@auth.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user : User = User.query.filter_by(username=form.username.data).first()

        if attempted_user and attempted_user.check_password(form.password.data):
            login_user(attempted_user)
            flash([f'Logged in successfully! Welcome to the club {attempted_user.username}'], category='success')
            return redirect(url_for('main.home'))

        else:
            flash(['Username and password do not match. Try again.'], category='danger')


    return render_template("auth/login.html", form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash(["You logged out"], category='info')
    return redirect(url_for('main.home'))