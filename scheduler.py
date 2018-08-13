from celery import Celery
from celery.schedules import crontab

import pandas as pd

from app.models import Report


app = Celery('scheduler', broker='pyamqp://guest@localhost//')


@app.task
def run_report(report_id):
    """
    TODO
    """
    report = Report.query.filter_by(id=report_id).first()
    df = pd.read_sql(report.query_text, r.create_engine())
    df.to_csv(f'{report.report_name}.csv', index=None)


def find_new_reports():
    """
    TODO
    """
    reports = Report.query.all()
    for r in reports:
        app.conf.beat_schedule = {
            r.report_name: {
                'task': 'scheduler.run_report'
                'schedule': crontab(hour=r.hour, minute=r.minute,
                                    day_of_week=r.day),
                'args': (r.id)
            }
        }
    return app.conf.beat_schedule