from flask import Flask, render_template

from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import PasswordField, StringField, TextAreaField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

from data import db_session
from data.jobs import Jobs
from data.users import User
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/Mars.sqlite")
    session = db_session.create_session()
    j = Jobs()
    u = User()
    app.run()


@app.route('/')
@app.route('/jobs_list')
def jobs_list():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template("index.html", jobs=jobs)


if __name__ == '__main__':
    main()
