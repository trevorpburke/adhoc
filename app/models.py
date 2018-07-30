from werkzeug.security import (generate_password_hash,
                               check_password_hash)

from app import db


class Configuration(db.Model):
    __tablename__ = 'configuration'
    id = db.Column(db.Integer, primary_key=True)
    config_name = db.Column(db.String(64), unique=True)
    username = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    hostname = db.Column(db.String(64))
    database = db.Column(db.String(64))
    port = db.Column(db.String(10))
    # TODO create DB relationships

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Report(db.Model):
    __tablename__ = 'report'
    id = db.Column(db.Integer, primary_key=True)
    report_name = db.Column(db.String(64), unique=True)
    query = db.Column(db.Text())
    # TODO create DB relationships


# class Scheduler(db.Model):
#     pass
    # TODO create scheduler that relates to Report model


# TODO handle alembic migrations
