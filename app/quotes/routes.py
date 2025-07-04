from flask import render_template
from . import quotes

@quotes.route('/all')
def quotes_page():
    return render_template('quotes/all_quotes.html')