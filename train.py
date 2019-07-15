#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-11 16:59:16
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import datetime
import random

import flask
from flask import render_template, redirect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

import helper
import config

logger = helper.getLogger('train')

app = flask.Flask('train')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)


class User(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    username = db.Column(db.String(64))
    gender = db.Column(db.Enum('male', 'female'))
    birthday = db.Column(db.DateTime())
    phone = db.Column(db.String(64))
    email = db.Column(db.String(64))
    website = db.Column(db.String(64))

    records = db.relationship('Record',
                              backref='user',
                              lazy=True)

    def __repr__(self):
        return '<User %r>' % self.name


class Course(db.Model):
    courseId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    tel = db.Column(db.String(64))
    website = db.Column(db.String(64))
    desc = db.Column(db.Text())

    records = db.relationship('Record',
                              backref='course',
                              lazy=True)

    def __repr__(self):
        return '<Course %r>' % self.name


class Record(db.Model):
    recordId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer,
                       db.ForeignKey(User.userId),
                       nullable=False)

    courseId = db.Column(db.Integer,
                         db.ForeignKey(Course.courseId),
                         nullable=False)
    logged = db.Column(db.DateTime())
    comment = db.Column(db.Text())

    def __repr__(self):
        return '<Post %r:%r:%r>' % (self.user.name,
                                    self.course.name,
                                    self.logged)


class UserModelView(ModelView):
    column_exclude_list = ('records')


class CourseModelView(ModelView):
    column_exclude_list = ('records')


class RecordModelView(ModelView):
    column_list = ('user.name', 'course.name', 'logged', 'comment')


# set optional booswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(UserModelView(User, db.session))
admin.add_view(CourseModelView(Course, db.session))
admin.add_view(RecordModelView(Record, db.session))


@app.route('/users', methods=['GET'])
def users():
    """Handle the class data
    """
    users = User.query.all()
    return render_template('users.html',
                           users=users)


@app.route('/courses', methods=['GET'])
def courses():
    """Handle the class data
    """
    courses = Course.query.all()
    return render_template('courses.html',
                           courses=courses)


@app.route('/records', methods=['GET'])
def records():
    """Handle the train data
    """
    records = Record.query.all()
    return render_template('records.html',
                           records=records)


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/')
def home():
    return redirect('/index')


def fakeData():
    config.DB_FILE.unlink()
    db.create_all()
    for inx in range(1, 11):
        user = User(name='name%r' % inx,
                    gender=random.choice(['male', 'female']))

        course = Course(name='course%r' % inx)

        post = Record(userId=inx,
                      courseId=inx,
                      logged=datetime.datetime.today())

        db.session.add(user)
        db.session.add(course)
        db.session.add(post)

    db.session.commit()


def main():
    fakeData()
    app.run(port=80, debug=True)


if __name__ == '__main__':
    main()
