from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

#Add quote form
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

#Filter quotes form
class FilterQuotes(FlaskForm):
    phrase = StringField(label="Enter phrase to filter by")
    select_category = SelectField(label="Filter by category", choices=[
        ('all', 'All'),
        ('motivation', 'Motivation'),
        ('success', 'Success'),
        ('relationships', 'Relationships'),
        ('love', 'Love'),
        ('life', 'Life'),
        ('happiness', 'Happiness'),
        ('philosophy', 'Philosophy'),
    ], default='all')
    submit_searching = SubmitField(label="Search")
