from flask.blueprints import Blueprint
from Managers.DatabaseManager import DatabaseManager
from Models.Lecturer import Lecturer
from Models.Interval import Interval
from Models.Subject import Subject
from Models.Group import Group
from Models.Schedule import Schedule
from flask import request, render_template
from extensions import db

schedules = Blueprint('schedules', __name__, template_folder='templates', static_folder='static')

@schedules.route('/lecturers/AddNote', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db_manager = DatabaseManager(db)
        db_manager.add_timetable(day=request.form.get('day'),
                                 interval_id=request.form.get('interval'),
                                 subject_id=request.form.get('subject'),
                                 lecturer_id=request.form.get('lecturer'),
                                 group_id=request.form.get('group'))
    return render_template('AddNote.html',
                           lecturers=Lecturer.query.all(),
                           intervals=Interval.query.all(),
                           subjects=Subject.query.all(),
                           groups=Group.query.all(),
                           schedule=Schedule.query.all()
                           )
