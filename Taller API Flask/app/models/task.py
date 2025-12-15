from . import db

from sqlalchemy.event import listen



class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __str__(self):
        return self.title

def insert_tasks(*args, **kwargs):
    db.session.add(
        Task(title="Task 1", description="This is the task 1", deadline="2021-01-01 12:00:00")
    )
    db.session.add(
        Task(title="Task 2", description="This is the task 2", deadline="2021-01-01 12:00:00")
    )
    db.session.add(
        Task(title="Task 3", description="This is the task 3", deadline="2021-01-01 12:00:00")
    )
    db.session.commit()

listen(Task.__table__, 'after_create', insert_tasks)