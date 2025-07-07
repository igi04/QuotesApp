from flask import render_template
from . import main
from app import db
from app.models import Quote

@main.route('/')
def home():
    return render_template("home.html")