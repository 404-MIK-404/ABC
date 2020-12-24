from flask.blueprints import Blueprint
from Managers.DatabaseManager import DatabaseManager
from Models.Lecturer import Lecturer
from Models.Interval import Interval
from Models.Subject import Subject
from Models.Schedule import Schedule
from Models.Group import Group
from flask import request, render_template
from extensions import db

lecturers = Blueprint('lecturers', __name__, template_folder='templates', static_folder='static')


@lecturers.route('/lecturers')
def index():
    return render_template('Index.html',
                           schedules=Schedule.query.all(),
                           lecturers=Lecturer.query.all(),
                           intervals=Interval.query.all(),
                           subjects=Subject.query.all(),
                           groups=Group.query.all())


@lecturers.route('/lecturers/see', methods=['POST'])
def See():
    week = None
    group_need = None
    if request.method == 'POST':

        print("Компьютер подключен")
        week=request.form.get('week')
        group_need= Group.query.filter_by(name=request.form.get('group')).first()
    return render_template('SeeSchedule.html',
                           schedules=Schedule.query.all(),
                           lecturers=Lecturer.query.all(),
                           intervals=Interval.query.all(),
                           subjects=Subject.query.all(),
                           groups=Group.query.all(),
                           week=week,
                           group_need=group_need)
