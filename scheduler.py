from celery import Celery
from celery.schedules import crontab

import pandas as pd

from app.models import Report


app = Celery('scheduler', broker='pyamqp://guest@localhost//')

app.config_from_object('celeryconfig')

@app.on_after_configure.connect
def check_new_reports(sender, **kwargs):
    sender.add_periodic_task(30.0, find_new_reports(),
                             name='find new reports every 30s')


@app.task
def run_report(report_id):
    """
    report_id: list

    celery beat task arguments are stored in list or tuple
    """
    for r in report_id:
        report = Report.query.filter_by(id=r).first()
        df = pd.read_sql(report.query_text, report.create_engine())
        df.to_csv(f'{report.report_name}.csv', index=None)


def find_new_reports():
    """
    TODO
    """
    reports = Report.query.all()
    for r in reports:
        if r.report_name not in app.conf.beat_schedule:
            app.conf.beat_schedule[r.report_name] = {
                'task': 'scheduler.run_report',
                'schedule': crontab(hour=r.hour, minute=r.minute,
                                    day_of_week=r.day),
                'args': [r.id]
            }

    return app.conf.beat_schedule
