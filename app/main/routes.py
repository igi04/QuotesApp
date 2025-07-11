from datetime import time
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from app import mail, db
from .forms import MailerSettingsForm
from . import main

@main.route('/')
def home():
    return render_template("home.html")

@main.route('/mailer', methods=['GET', 'POST'])
@login_required
def emailer_page():
    form = MailerSettingsForm()
    if form.validate_on_submit():

        if form.daily_quote_enabled.data and form.daily_quote_time.data is None:
            flash(["Please select a preferred delivery time."], "warning")
            return redirect(url_for('main.emailer_page'))

        current_user.daily_quote_enabled = form.daily_quote_enabled.data
        current_user.daily_quote_time = form.daily_quote_time.data
        db.session.commit()

        flash(['Your settings has been updated'], category='success')
        return redirect(url_for('main.emailer_page'))

    elif request.method == "GET":
        form.daily_quote_enabled.data = current_user.daily_quote_enabled
        form.daily_quote_time.data = current_user.daily_quote_time

        # msg = Message(
        #     subject="Test Quote Delivery",
        #     recipients=["igor.gosrit@gmail.com"],
        #     body="Here is your daily dose of inspiration:\n\n\"Stay hungry, stay foolish.\" – Steve Jobs"
        # )
        #
        # try:
        #     mail.send(msg)
        #     flash(["Mail sent successfully!"], "success")
        # except Exception as e:
        #     flash([f"Something went wrong: {str(e)}"], "danger")
        #
        # return redirect(url_for("main.home"))

    return render_template('main/mailer.html', form=form)