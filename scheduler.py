from collections import namedtuple

import pandas as pd
from celery import Celery

from app.models import Configuration, Report
# app = Celery('schedule', broker='pyamqp://guest@localhost//')


def run_reports():
    """
    TODO
    """
    Reports = namedtuple('Report', 'report_name query engine')
    reports = [Reports(r.report_name, r.query_text, r.get_engine())
               for r in Report.query.all()]

    for r in reports:
        df = pd.read_sql(r.query, r.engine)
        df.to_csv(f'{r.report_name}.csv', index=None)
