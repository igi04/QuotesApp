from flask import render_template, redirect, flash, url_for, request
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
                                category=form.category.data,
                                is_private=form.is_private.data == "True",
                                user_id=current_user.id)
        db.session.add(quote_to_create)
        db.session.commit()
        flash(["You added your own quote"], category='success')
        return redirect(url_for("quotes.quotes_page"))
    return render_template('quotes/add_quote.html', form=form)

@quotes.route('/my-quotes')
@login_required
def user_quotes():
    private_quotes = Quote.query.filter_by(user_id=current_user.id).all()
    return render_template('quotes/my_quotes.html', quotes=private_quotes)

@quotes.route('/like/<int:quote_id>', methods=['GET', 'POST'])
@login_required
def like_quote(quote_id):
    quote = Quote.query.get_or_404(quote_id)

    if current_user in quote.liked_by:
        quote.liked_by.remove(current_user)
        flash(['Removed from liked quotes'], category='warning')

    else:
        quote.liked_by.append(current_user)
        flash(["Quote liked!"], "success")

    db.session.commit()
    return redirect(request.referrer or url_for('quotes.quotes_page'))

@quotes.route('/liked-quotes')
@login_required
def liked_quotes():
    return render_template('quotes/liked_quotes.html', liked_quotes=current_user.liked_quotes.all())
