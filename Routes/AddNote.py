from flask.blueprints import Blueprint
from Managers.DatabaseManager import DatabaseManager
from Models.Lecturer import Lecturer
from Models.Interval import Interval
from Models.Subject import Subject
from Models.Group import Group
from Models.Schedule import Schedule
from flask import request, render_template
from extensions import db

db_manager = DatabaseManager(db)
schedules = Blueprint('schedules', __name__, template_folder='templates', static_folder='static')


@schedules.route('/lecturers/Schedule', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        intervals = request.form.get('interval')
        subjects = request.form.get('subject')
        lecturers = request.form.get('lecturer')
        groups = request.form.get('group')
        if lecturers and intervals and groups and subjects:
            lecturer_id = Lecturer.query.filter_by(name_lecturer=request.form.get('lecturer')).first()
            interval_id = Interval.query.filter_by(begintime=request.form.get('interval')).first()
            subject_id = Subject.query.filter_by(name=request.form.get('subject')).first()
            group_id = Group.query.filter_by(name=groups).first()
            db_manager.add_schedule(day=request.form.get('day'),
                                    chet_notchet=request.form.get('week'),
                                    interval_id=interval_id.id,
                                    subject_id=subject_id.id,
                                    lecturer_id=lecturer_id.id,
                                    group_id=group_id.id)


    return render_template('AddNote.html',
                           lecturers=Lecturer.query.all(),
                           intervals=Interval.query.all(),
                           subjects=Subject.query.all(),
                           groups=Group.query.all(),
                           schedules=Schedule.query.all()
                           )
