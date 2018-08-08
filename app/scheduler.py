from collections import namedtuple

import pandas as pd

from app.models import Report


def run_report(report_id):
    """
    TODO
    """
    report = Report.query.filter_by(id=report_id).first()
    df = pd.read_sql(report.query_text, r.create_engine())
    df.to_csv(f'{report.report_name}.csv', index=None)

