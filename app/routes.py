from flask import render_template, redirect, url_for
from app import app
from app.forms import ConfigurationForm, ReportForm


@app.route('/')
@app.route('/index')
def index():
    return "Test"


@app.route('/configuration', methods=['GET', 'POST'])
def configuration():
    form = ConfigurationForm()
    if form.validate_on_submit():
        # keep this redirect here for a bit till I figure out what to do
        # with it
        return redirect(url_for('index'))
    return render_template('configuration.html', form=form)

@app.route('/report', methods=['GET', 'POST'])
def report():
    form = ReportForm()
    if form.validate_on_submit():
        # keep this redirect here for a bit till I figure out what to do
        # with it
        return redirect(url_for('index'))
    return render_template('report.html', form=form)
