from flask import render_template, redirect, url_for
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
                               hostname=form.hostname.data,
                               database=form.database.data,
                               port=form.port.data)
        config.set_password(form.password.data)
        db.session.add(config)
        db.session.commit()
        # keep this redirect here for a bit till I figure out what to do
        # with it
        return redirect(url_for('index'))
    return render_template('configuration.html', form=form)

@app.route('/report', methods=['GET', 'POST'])
def report():
    form = ReportForm()
    if form.validate_on_submit():
        report = Report(report_name=form.report_name.data,
                        query=form.query.data)
        db.session.add(report)
        db.session.commit()
        # keep this redirect here for a bit till I figure out what to do
        # with it
        return redirect(url_for('index'))
    return render_template('report.html', form=form)
