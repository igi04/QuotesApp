from flask_wtf import FlaskForm
from wtforms import BooleanField, TimeField, SubmitField
from wtforms.validators import DataRequired, Optional

class MailerSettingsForm(FlaskForm):
    daily_quote_enabled = BooleanField('Enable daily mails')
    daily_quote_time = TimeField("Preferred delivery time", validators=[Optional()])
    submit = SubmitField('Save Settings')