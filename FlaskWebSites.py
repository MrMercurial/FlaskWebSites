import sqlite3
from flask import Flask,request,g,session,redirect,url_for,render_template
from flask.ext.bootstrap import Bootstrap

app=Flask(__name__)
bootstrap=Bootstrap(app)

@app.route('/')
def index():
    useragent=request.headers.get('User-Agent')
    return 'Hello World! %s'%useragent

@app.route('/user/<username>')
def Hello_User(username):
    return render_template('user.html',name=username)

if __name__ =="__main__":
    app.run()