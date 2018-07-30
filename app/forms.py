from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField,
                     PasswordField, TextAreaField)
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired


class ConfigurationForm(FlaskForm):
    config_name = StringField('Configuration Name',
                              validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    hostname = StringField('Hostname', validators=[DataRequired()])
    database = StringField('Database', validators=[DataRequired()])
    port = StringField('Port', validators=[DataRequired()])
    submit = SubmitField('Submit Config')

class ReportForm(FlaskForm):
    report_name = StringField('Report Name',
                              validators=[DataRequired()])
    query = TextAreaField('Query', validators=[DataRequired()],
                          widget=TextArea())
    submit = SubmitField('Submit Report')
