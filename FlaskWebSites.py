import sqlite3
from flask import Flask,request,g,session,redirect,url_for

app=Flask(__name__)

@app.route('/')
def index():
    useragent=request.headers.get('User-Agent')
    return 'Hello World! %s'%useragent

@app.route('/user/<username>')
def Hello_User(username):
    return 'Hello %s'%username

if __name__ =="__main__":
    app.run(debug=True)