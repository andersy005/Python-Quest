from flask import Flask
from flask import url_for
from flask.ext.sqlalchemy import SQLAlchemy
import sched.models import Base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sched.db'

# Use Flask-SQLAlchemy for its engine and session
# configuration. Load the extension, giving it the app object,
# and override its default Model class with the pure
# SQLAlchemy declarative Base class.

db = SQLAlchemy(app)
db.Model = Base

@app.route('/')
def hello():
    return 'Hello World! '

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/appointments')
def appointment_list():
    return 'Listing of all appointments we have.'


@app.route('/appointments/<int:appointment_id>/')
def appointment_detail(appointment_id):
    #edit_url = url_for('appointment_edit', appointment_id=appointment_id)
    return 'Detail of appointment   #{}.'.format(appointment_id)
    #return edit_url


@app.route('/appointments/<int:appointment_id>/edit/', methods=['GET', 'POST'])
def appointment_edit(appointment_id):
    return 'Form to edit appointment #.'.format(appointment_id)


@app.route('/appointments/create/', methods=['GET', 'POST'])
def appointment_create():
    return 'Form to create a new appointment.'


@app.route('/appointments/<int:appointment_id>/delete/', methods=['DELETE'])
def appointment_delete(appointment_id):
    raise NotImplementedError('DELETE')




