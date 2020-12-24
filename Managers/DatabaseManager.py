from Models.Lecturer import Lecturer
from Models.Interval import Interval
from Models.Schedule import Schedule
from Models.Subject import Subject
from Models.Group import Group

class DatabaseManager:
    def __init__(self, db):
        self.db = db

    def add_lecturer(self, **kwargs):
        lecturer = Lecturer(name_lecturer=kwargs["name_lecturer"],
                            )
        self.db.session.add(lecturer)
        self.db.session.commit()

    def add_interval(self,**kwargs):
        interval = Interval(begintime=kwargs["begintime"])
        self.db.session.add(interval)
        self.db.session.commit()

    def add_schedule(self, **kwargs):
        timetable = Schedule(day=kwargs["day"],
                             chet_notchet=kwargs["chet_notchet"],
                             interval_id=kwargs["interval_id"],
                             subject_id=kwargs["subject_id"],
                             lecturer_id=kwargs["lecturer_id"],
                             group_id=kwargs["group_id"]
                             )
        self.db.session.add(timetable)
        self.db.session.commit()

    def add_subject(self, **kwargs):
        subject = Subject(name=kwargs["name"]
                          )
        self.db.session.add(subject)
        self.db.session.commit()

    def add_group(self,**kwargs):
        group = Group(name=kwargs["name"])
        self.db.session.add(group)
        self.db.session.commit()