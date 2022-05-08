# from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# if os.path.exists(dotenv_path):
#     load_dotenv(dotenv_path)
# app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('SQLALCHEMY_DATABASE_URI')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    create_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self) -> str:
        return f'<Member {self.firstname}>'


@app.route('/')
def index():
    members = Member.query.all()
    return render_template('index.html', members=members)


@app.route('/аpply', methods=('GET', 'POST'))
def apply():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        member = Member(firstname=firstname,
                          lastname=lastname,
                          email=email,
                          age=age)
        db.session.add(member)
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