from flask.blueprints import Blueprint
from Managers.DatabaseManager import DatabaseManager
from Models.Lecturer import Lecturer
from Models.Interval import Interval
from flask import request, render_template
from extensions import db

addLecturers = Blueprint('addLecturers', __name__, template_folder='templates', static_folder='static')


@addLecturers.route("/lecturers", methods=['GET', 'POST'])
def AddLecturers():
    if request.method == 'POST':
        db_manager = DatabaseManager(db)
        db_manager.add_lecturer(first_name=request.form.get('first_name'), last_name=request.form.get('last_name'),
                                patronymic=request.form.get('patronymic'))
    return render_template('Index.html',
                           lecturers=Lecturer.query.all(),
                           intervals=Interval.query.all())
