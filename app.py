from flask import Flask
from flask import redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from Models.Interval import Interval
from Models.Group import Group
from Models.Schedule import Schedule
from Models.Lecturer import Lecturer
from Models.Subject import Subject

from Routes.AddLecturers import addLecturers
from Routes.Lecturers import lecturers

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.register_blueprint(lecturers)
app.register_blueprint(addLecturers)

if __name__ == '__main__':
    app.run()

