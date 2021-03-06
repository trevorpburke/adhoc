from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField,
                     PasswordField, TextAreaField, SelectField, IntegerField)
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, InputRequired, NumberRange


SQL_DIALECTS = [('postgresql', 'PostgreSQL'), ('mysql', 'MySQL')]

HOURS = [(0, '12 AM'), (1, '1 AM'), (2, '2 AM'), (3, '3 AM'),
         (4, '4 AM'),(5, '5 AM'), (6, '6 AM'), (7, '7 AM'), (8, '8 AM'),
         (9, '9 AM'), (10, '10 AM'), (11, '11 AM'), (12, '12 AM'),
         (13, '1 PM'), (14, '2 PM'), (15, '3 PM'), (16, '4 PM'),
         (17, '5 PM'), (18, '6 PM'), (19, '7 PM'), (20, '8 PM'),
         (21, '9 PM'), (22, '10 PM'), (23, '11 PM')]

MINUTES = [(0, 'On the hour'), (15, 'At XX:15'), (30, 'At XX:30'),
           (45, 'At XX:45')]

DAYS = [(0, 'Every Sunday'), (1, 'Every Monday'),
        (2, 'Every Tuesday'), (3, 'Every Wednesday'),
        (4, 'Every Thursday'), (5, 'Every Friday'),
        (6, 'Every Saturday')]

class ConfigurationForm(FlaskForm):
    config_name = StringField('Configuration Name',
                              validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    # TODO encrypt password
    password = PasswordField('Password', validators=[DataRequired()])
    hostname = StringField('Hostname', validators=[DataRequired()])
    database = StringField('Database', validators=[DataRequired()])
    port = StringField('Port', default='5432', validators=[DataRequired()])
    dialect = SelectField('SQL Dialect', choices=SQL_DIALECTS,
                          validators=[DataRequired()])
    submit = SubmitField('Submit Config')

class ReportForm(FlaskForm):
    report_name = StringField('Report Name',
                              validators=[DataRequired()])
    config_id = SelectField('Configuration Name',
                               coerce=int,
                               validators=[DataRequired()])
    hour = SelectField('Report Hour', choices=HOURS, coerce=int,
                        validators=[InputRequired()])
    minute = IntegerField('Report Minute',
                         validators=[InputRequired(), NumberRange(0, 59)])
    day = SelectField('Report day', choices=DAYS, coerce=int,
                       validators=[InputRequired()])
    query_text = TextAreaField('Query', validators=[DataRequired()],
                          widget=TextArea())
    submit = SubmitField('Submit Report')

