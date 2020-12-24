from flask.blueprints import Blueprint
from Managers.DatabaseManager import DatabaseManager
from Models.Group import Group
from flask import request, render_template
from extensions import db

add_groups = Blueprint('add_groups', __name__, template_folder='templates', static_folder='static')


@add_groups.route('/lecturers/AddGroups', methods=['GET', 'POST'])
def AddGroup():
    if request.method == 'POST':
        db_manager = DatabaseManager(db)
        db_manager.add_group(name=request.form.get('group'))
    return render_template('GroupAdd.html',groups=Group.query.all())
