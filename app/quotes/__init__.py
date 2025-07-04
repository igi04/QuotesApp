from flask import Blueprint

quotes = Blueprint('quotes', __name__, url_prefix='/quotes')

from . import routes