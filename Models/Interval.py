from extensions import db


class Interval(db.Model):
    __tablename__ = 'interval'
    id = db.Column(db.Integer, primary_key=True)
    begintime = db.Column(db.String(30))