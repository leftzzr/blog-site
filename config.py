# -*- coding: utf-8 -*-
# @Time    : 2022/5/16 12:37
# @Author  : 张梓锐
# @File    : config.py
# @Software: PyCharm 
# @Content : 自定义配置文件

JSON_AS_ASCII = False

# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'flask_project'
USERNAME = 'root'
PASSWORD = 'merry'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_DATABASE_MODIFICATIONS = True

SECRET_KEY = "cgjftrysbhui2135jhfg"


# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "2017159475@qq.com"
MAIL_PASSWORD = "degnstwerjnubafb"
MAIL_DEFAULT_SENDER = "2017159475@qq.com"

















