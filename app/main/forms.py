from flask_wtf import FlaskForm
from wtforms import BooleanField, TimeField, SubmitField, SelectField
from wtforms.validators import Optional

#Mailer Settings Form
class MailerSettingsForm(FlaskForm):
    daily_quote_enabled = BooleanField('Enable daily mails')
    daily_quote_time = TimeField("Preferred delivery time", validators=[Optional()])
    daily_quote_category = SelectField(label="Choose category of quotes", choices=[
        ('all', 'All'),
        ('liked', 'Liked by me'),
        ('motivation', 'Motivation'),
        ('success', 'Success'),
        ('relationships', 'Relationships'),
        ('love', 'Love'),
        ('life', 'Life'),
        ('happiness', 'Happiness'),
        ('philosophy', 'Philosophy'),
    ])
    submit = SubmitField('Save Settings')