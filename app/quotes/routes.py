from flask import render_template, redirect, flash, url_for
from flask_login import login_required, current_user
from . import quotes
from .forms import AddQuote
from app.models import Quote
from app import db

@quotes.route('/all')
def quotes_page():
    all_quotes = Quote.query.filter_by(is_private=False).all()
    return render_template('quotes/all_quotes.html', quotes=all_quotes)

@quotes.route('/add', methods=['GET', 'POST'])
@login_required
def add_quote_page():
    form = AddQuote()
    if form.validate_on_submit():
        quote_to_create = Quote(content=form.content.data,
                                author_name=form.author_name.data,
                                is_private=form.is_private.data == "True",
                                user_id=current_user.id)
        db.session.add(quote_to_create)
        db.session.commit()
        flash(["You added your own quote"], category='success')
        return redirect(url_for("quotes.quotes_page"))
    return render_template('quotes/add_quote.html', form=form)