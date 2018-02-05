"""
SQLAlchemy的使用示例
pip install flask-sqlalchemy
"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import datetime

# 连接
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:pwd@localhost:port/database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# 模型示例
class User(db.Model):
    '''
    会员数据模型
    '''
    __tablename__ = 'user'
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(11), unique=True)
    info = db.Column(db.Text)
    face = db.Column(db.String(255))
    addtime = db.Column(db.DateTime, index=True, default=datatime.utcnow)
    uuid = db.Column(db.String(255), unique=True)
    # 外键关系关联
    userlogs = db.relationship('Userlog', backref='user')

    def __repr__(self):
        return "<User: {}>".format(self.name)


class Userlog(db.Model):
    '''
    会员登陆日志
    '''
    __tablename__ = "userlog"
    id = db.Column(db.integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ip = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<Userlog: {}>".format(self.id)
