from flask import render_template, redirect, url_for, flash
from app import app, db
from app.models import Configuration, Report
from app.forms import ConfigurationForm, ReportForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/configuration', methods=['GET', 'POST'])
def configuration():
    form = ConfigurationForm()
    if form.validate_on_submit():
        config = Configuration(config_name=form.config_name.data,
                               username=form.username.data,
                               password=form.password.data,
                               hostname=form.hostname.data,
                               database=form.database.data,
                               port=form.port.data,
                               dialect=form.dialect.data)
        db.session.add(config)
        db.session.commit()
        # keep this redirect here for a bit till I figure out what to do
        # with it
        return redirect(url_for('index'))
    return render_template('configuration.html', form=form)

@app.route('/report', methods=['GET', 'POST'])
def report():

    form = ReportForm()
    form.config_id.choices =[(c.id, c.config_name) for c in Configuration.\
                     query.with_entities(Configuration.id,
                        Configuration.config_name).all()]
    if form.validate_on_submit():
        report = Report(report_name=form.report_name.data,
                        config_id=form.config_id.data,
                        hour=form.hour.data,
                        day=form.day.data,
                        minute=form.minute.data,
                        query_text=form.query_text.data)
        db.session.add(report)
        db.session.commit()
        # keep this redirect here for a bit till I figure out what to do
        # with it
        return redirect(url_for('index'))
    return render_template('report.html', form=form)


@app.route('/configuration/<config>', methods=['GET'])
def get_config(config):
    pass

@app.route('/report/<report_name>', methods=['GET'])
def get_report(report_name):
    pass



