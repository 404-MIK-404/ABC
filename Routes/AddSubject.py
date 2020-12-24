from flask.blueprints import Blueprint
from Managers.DatabaseManager import DatabaseManager
from Models.Subject import Subject
from flask import request, render_template
from extensions import db

add_subject = Blueprint('add_subject', __name__, template_folder='templates', static_folder='static')


@add_subject.route('/lecturers/AddSubject', methods=['GET', 'POST'])
def AddSubject():
    if request.method == 'POST':
        db_manager = DatabaseManager(db)
        db_manager.add_subject(name=request.form.get('subject'))

    return render_template('AddSubject.html', subjects=Subject.query.all())