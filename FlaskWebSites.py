#encoding=utf-8
import sqlite3,os
from flask import Flask,request,g,session,redirect,url_for,render_template
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
# from flask.ext.bootstrap import Bootstrap
# from flask.ext.sqlalchemy import SQLAlchemy

basedir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
DATABASE=os.path.join(basedir,'data.db')



def connect_db():
    return sqlite3.connect(DATABASE)
# db=SQLAlchemy(app)

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

# bootstrap=Bootstrap(app)

@app.before_first_request
def create_db():
    g.db=connect_db()
    g.db.execute(
        """create table if not exists articles(id INTEGER primary KEY autoincrement,title VARCHAR (128),article VARCHAR (512))""")
    g.db.commit()
@app.before_request
def before_request():
    g.db=connect_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/')
def index():
    useragent=request.headers.get('User-Agent')
    return 'Hello World! %s'%useragent

@app.route('/user/<username>')
def Hello_User(username):
    return render_template('index.html',name=username)

@app.route('/api/aa',methods=['GET','POST'])
def submit_user():
    if request.method=='POST':
        title=request.form.get('username',119)
        # artilces=['diyibiasnfweo','sdafew']
        article=request.form.get('txt',200)
        print title
        print article

        # with sqlite3.connect(DATABASE) as con:
        #     cur = con.cursor()
        #     cur.execute("INSERT INTO articles(id,title,article) VALUES (?,?,?)",(1,title,article) )
        #
        #     con.commit()
        #     msg = "Record successfully added"


        ############################################3
        # print inputname
        g.db.execute("INSERT INTO articles(title,article) VALUES (?,?)",(title,article))
        g.db.commit()

        cur = g.db.cursor()
        # 用游标来查询就可以获取到结果
        cur.execute("select * from articles")
        # 获取所有结果
        res = cur.fetchall()
        return render_template('index.html',articles=res)
        con.close()

@app.route('/api/facecompare',methods=['POST'])
def facecompare():
    if request.method=="POST":
        print "-----------begin--------"
        print request.form
        return "ok"
@app.route('/face')
def face():
    return render_template('face.html')

if __name__ =="__main__":
    app.run(debug=True)