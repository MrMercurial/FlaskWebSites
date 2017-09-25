#encoding=utf-8
import sqlite3,os
from flask import Flask,request,g,session,redirect,url_for,render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

basedir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

db=SQLAlchemy(app)

# class Role(db.Model):
#     __tablename__='roles'
#     id=db.column(db.Integer,primary_key=True)
#     name=db.column(db.String(64),unique=True)
#     users=db.relationship('User',backref='role')
#
#     def __repr__(self):
#         return '<Role %r>'%self.name
#
# class User(db.Model):
#     __tablename__='users'
#     id=db.column(db.Integer,primary_key=True)
#     username=db.column(db.String(64))
#     role_id=db.column(db.Integer,db.ForeignKey('roles.id'))
#
#     def __repr__(self):
#         return '<User %r>'%self.username

bootstrap=Bootstrap(app)

@app.route('/')
def index():
    useragent=request.headers.get('User-Agent')
    return 'Hello World! %s'%useragent

@app.route('/user/<username>')
def Hello_User(username):
    return render_template('index.html',name=username)

if __name__ =="__main__":
    app.run()