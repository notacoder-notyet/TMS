from datetime import datetime

# from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy.orm import relationship, backref

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://test:test@localhost/test'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# load_dotenv()

db = SQLAlchemy(app)

from models import Member, Event, event_member

@app.route('/')
def index():
    events = Event.query.all()
    return render_template('index.html', events=events)


@app.route('/аpply', methods=('GET', 'POST'), endpoint='apply')
def apply():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        age = int(request.form['age'])
        member = Member(first_name=first_name,
                          last_name=last_name,
                          email=email,
                          age=age)
        event_name = request.form['event_name']            
        db.session.add(member)
        event = db.session.query(Event).filter(Event.event_name == event_name).first()
        member.membership.append(event)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('apply.html')


@app.route('/<int:member_id>', endpoint='member')
def member(member_id):
    member = Member.query.get_or_404(member_id)
    return render_template('member.html', member=member)


@app.route('/members', endpoint='members')
def member():
    members = Member.query.all()
    return render_template('members.html', members=members)


@app.route('/event-info', endpoint='info')
def event_info():
    return render_template('info.html')


if __name__ == "__main__":
    app.run(debug=True)