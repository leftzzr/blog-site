# -*- coding: utf-8 -*-
# @Time    : 2022/5/16 12:42
# @Author  : 张梓锐
# @File    : extends.py
# @Software: PyCharm 
# @Content : 用于存放易于循环调用的语句

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
db = SQLAlchemy()
mail = Mail()
