from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from app import db, Quote
from .forms import MailerSettingsForm
from . import main

#Main page
@main.route('/')
def home():
    return render_template("main/home.html")

#Emailer page
@main.route('/mailer', methods=['GET', 'POST'])
@login_required
def emailer_page():
    form = MailerSettingsForm()

    if form.validate_on_submit():

        #Validation of emailer settings
        if form.daily_quote_enabled.data and not form.daily_quote_time.data:
            flash(["Please select a preferred delivery time."], "warning")
            return redirect(url_for('main.emailer_page'))

        if form.daily_quote_enabled.data:
            selected_category = form.daily_quote_category.data

            if selected_category == "liked":
                if not current_user.liked_quotes.first():
                    flash(["You have no liked quotes. Choose a different category or like one."], "danger")
                    return redirect(url_for('main.emailer_page'))

            elif selected_category != "all":
                quote_exists = Quote.query.filter_by(category=selected_category).first()
                if not quote_exists:
                    flash(["No quotes found in this category. Choose a different one."], "danger")
                    return redirect(url_for('main.emailer_page'))

        #Commit changes to database
        previous_enabled = current_user.daily_quote_enabled
        current_user.daily_quote_enabled = form.daily_quote_enabled.data
        current_user.daily_quote_time = form.daily_quote_time.data
        current_user.daily_quote_category = form.daily_quote_category.data
        db.session.commit()

        if form.daily_quote_enabled.data and not previous_enabled:
            flash(['You enabled email function'], 'success')
        elif not form.daily_quote_enabled.data and previous_enabled:
            flash(['You disabled email function'], 'danger')
        else:
            flash(['You changed settings successfully'], 'success')

        return redirect(url_for('main.emailer_page'))

    elif request.method == "GET":
        # Clear the form if daily quote func is disabled
        if not current_user.daily_quote_enabled and (
               current_user.daily_quote_time is not None or current_user.daily_quote_category != "all"):
            current_user.daily_quote_time = None
            current_user.daily_quote_category = "all"
            db.session.commit()

        #Fill form with initial data on GET method
        form.daily_quote_enabled.data = current_user.daily_quote_enabled
        form.daily_quote_time.data = current_user.daily_quote_time
        form.daily_quote_category.data = current_user.daily_quote_category

    return render_template('main/mailer.html', form=form)
