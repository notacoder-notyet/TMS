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
    members = Member.query.all()
    return render_template('index.html', members=members)


@app.route('/аpply-to-<int:event_id>', methods=('GET', 'POST'), endpoint='apply')
def apply():
    if request.method == 'POST':
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        member = Member(firstname=first_name,
                          lastname=last_name,
                          email=email,
                          age=age)
        # eventname = request.form['event']            
        db.session.add(member)
        # event = db.session.query(Event).filter(Event.event_name == eventname).all()
        
        # event.membership.append(member)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('apply.html')


@app.route('/<int:member_id>', endpoint='member')
def member_info(member_id):
    member = Member.query.get_or_404(member_id)
    return render_template('member.html', member=member)


@app.route('/event-info', endpoint='info')
def event_info():
    return render_template('info.html')


if __name__ == "__main__":
    app.run(debug=True)