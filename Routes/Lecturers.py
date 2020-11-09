from flask.blueprints import Blueprint
from Managers.DatabaseManager import DatabaseManager
from Models.Lecturer import Lecturer
from Models.Interval import Interval
from flask import request, render_template
from extensions import db

lecturers = Blueprint('lecturers', __name__, template_folder='templates', static_folder='static')


@lecturers.route('/lecturers')
def index():
    return render_template('Index.html', lecturers=Lecturer.query.all(),intervals=Interval.query.all())

