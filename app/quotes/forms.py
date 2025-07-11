from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from app.models import Quote, User


class AddQuote(FlaskForm):
    content = StringField(label="Quote", validators=[DataRequired()])
    author_name = StringField(label="Author of the quote", validators=[DataRequired()])
    category = SelectField(label="Category", choices=[
        ('motivation', 'Motivation'),
        ('success', 'Success'),
        ('relationships', 'Relationships'),
        ('love', 'Love'),
        ('life', 'Life'),
        ('happiness', 'Happiness'),
        ('philosophy', 'Philosophy'),
    ])

    is_private = SelectField(label="Visibility",
                             choices=[('True', 'Private (only you)'), ('False', 'Public (everyone)')])
    add_quote = SubmitField(label="Add quote")
