from sqlalchemy import create_engine

from app import db


class Configuration(db.Model):
    __tablename__ = 'configuration'
    id = db.Column(db.Integer, primary_key=True)
    config_name = db.Column(db.String(64), unique=True)
    username = db.Column(db.String(64))
    # TODO encrypt password
    password = db.Column(db.String(128))
    hostname = db.Column(db.String(64))
    database = db.Column(db.String(64))
    port = db.Column(db.String(10))
    dialect = db.Column(db.String(50))
    reports = db.relationship('Report', backref='report', lazy=True)

    def create_engine(self):
        engine = create_engine(f"{self.dialect}://{self.username}:{self.password}@{self.hostname}:{self.port}/{self.database}")
        return engine


class Report(db.Model):
    __tablename__ = 'report'
    id = db.Column(db.Integer, primary_key=True)
    report_name = db.Column(db.String(64), unique=True)
    config_id = db.Column(db.Integer, db.ForeignKey('configuration.id'),
                            nullable=False)
    hour = db.Column(db.Integer)
    minute = db.Column(db.Integer)
    day = db.Column(db.Integer)
    query_text = db.Column(db.Text())

    def get_engine(self):
        report_config = Configuration.query.filter_by(id=self.config_id).first()
        engine = report_config.create_engine()
        return engine

