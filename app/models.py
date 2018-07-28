from app import db

class Configuration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    config_name = db.Column(db.String(64), unique=True)
    username = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    hostname = db.Column(db.String(64))
    database = db.Column(db.String(64))
    port = db.Column(db.String(10))


class Report(db.model):
    id = db.Column(db.Integer, primary_key=True)
    report_name = db.Column(db.String(64), unique=True)
    query = db.Column(db.Text())

