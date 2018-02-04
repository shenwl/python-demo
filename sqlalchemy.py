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
    网站会员数据模型
    '''
    __tablename__ = 'user'
    id = db.Column(db.integer, primary_key=True)    # 编号
    name = db.Column(db.String(100), unique=True)   # 昵称
    pwd = db.Column(db.String(100))             
    email = db.Column(db.String(100), unique=True)  
    phone = db.Column(db.String(11), unique=True)
    info = db.Column(db.Text)
    face = db.Column(db.String(255))                # 头像
    addtime = db.Column(db.DateTime, 
            index=True, default=datetime.utcnow)    # 注册时间
    uuid = db.Column(db.String(255), unique=True)   # 唯一标识
