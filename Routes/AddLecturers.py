from flask.blueprints import Blueprint
from Managers.DatabaseManager import DatabaseManager
from Models.Lecturer import Lecturer
from Models.Interval import Interval
from flask import request, render_template
from extensions import db

addLecturers = Blueprint('addLecturers', __name__, template_folder='templates', static_folder='static')


@addLecturers.route("/lecturers/AddLecturers", methods=['GET', 'POST'])
def AddLecturers():
    if request.method == 'POST':
        db_manager = DatabaseManager(db)
        db_manager.add_lecturer(name_lecturer=request.form.get('name_lecturer'))
    return render_template('LecturerAdd.html',
                           lecturers=Lecturer.query.all())
