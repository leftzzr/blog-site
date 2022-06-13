# -*- coding: utf-8 -*-
# @Time    : 2022/5/17 22:13
# @Author  : 张梓锐
# @File    : decorators.py
# @Software: PyCharm 
# @Content :
from flask import g, redirect, url_for
from functools import wraps


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if hasattr(g, 'user'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for("user.login"))
    return wrapper