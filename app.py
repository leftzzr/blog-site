# -*- coding: utf-8 -*-
# @Time    : 2022/5/16 12:29
# @Author  : 张梓锐
# @File    : app.py
# @Software: PyCharm 
# @Content : 基于flask的在线问答平台

from flask import Flask, session, g
import config
from extends import db, mail
from blueprints import user_bp, qa_bp
from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manager
from models import User_Model


app = Flask(__name__)
# manager = Manager(app)

app.config.from_object(config)

db.init_app(app)
mail.init_app(app)
migrate = Migrate(app, db)
#manager.add_command('db', MigrateCommand)

app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)


@app.before_request
def before_request():
    user_id = session.get("user_id")
    if user_id:
        try:
            user = User_Model.query.get(user_id)
            # 给g绑定一个叫做user的变量，它的值是user这个变量
            g.user = user
        except:
            g.user = None


# 请求来了-> before_request -> 视图函数 -> 视图函数中返回模板 -> context_processor
@app.context_processor
def context_processor():
    if hasattr(g, "user"):
        return {"user": g.user}
    else:
        return {}


if __name__ == '__main__':
 #   manager.run()
    app.run()
