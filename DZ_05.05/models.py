from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)


event_member = db.Table('event_member', 
    db.Column('member_id', db.Integer, db.ForeignKey('members.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('events.id'))
)


class Member(db.Model):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    membership = db.relationship("Event", secondary=event_member, backref='memberships')

    def __repr__(self) -> str:
        return f'<Member {self.first_name}>'


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), nullable=False)
    event_info = db.Column(db.String(300), nullable=False)
    event_date = db.Column(db.DateTime)

    def __repr__(self) -> str:
        return f'<Event {self.event_name}>'

# db.create_all() #была тут только для однократного создания таблицы, т.к. в консоли плевалась ошибками
# oleg = Member(first_name='Oleg', last_name='Klykov', age=20, email='oleg@mail.ru')
# neoleg = Member(first_name='neOleg', last_name='neKlykov', age=21, email='neOleg@mail.ru')
# test = Member(first_name='Test', last_name='Test', age=100, email='test@mail.ru')
# event1 = Event(event_name='Event-1', event_info='Some Event-1')
# event2 = Event(event_name='Event-2', event_info='Some Event-2')
# db.session.add_all([oleg, neoleg, test, event1, event2])
# # eventname = 'Event-1'
# event = db.session.query(Event).filter(Event.event_name == 'Event-1').first()
# print(event)
# oleg.membership.append(event)
# db.session.commit()