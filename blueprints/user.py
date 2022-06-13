# -*- coding: utf-8 -*-
# @Time    : 2022/5/16 12:48
# @Author  : 张梓锐
# @File    : user.py
# @Software: PyCharm 
# @Content : 用户进程相关

import datetime, string, random

from extends import mail, db
from flask_mail import Message
from models import EmailCaptchaModel,User_Model
from .forms import RegisterForm,LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (Blueprint,
                   render_template,
                   request,
                   redirect,
                   url_for,
                   jsonify,
                   session,
                   flash)

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = User_Model.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                session['user_id'] = user.id
                return redirect("/")
            else:
                flash("邮箱或密码错误")
                return redirect(url_for("user.login"))
        else:
            flash("邮箱或密码格式错误")
            return redirect(url_for("user.login"))


@bp.route('/logout')
def logout():
    # 清除session中所有的数据
    session.clear()
    return redirect(url_for('user.login'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            hash_password = generate_password_hash(password)
            user = User_Model(email=email, username=username, password=hash_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("user.login"))
        else:
            return redirect(url_for("user.register"))


@bp.route('/captcha', methods=["POST"])
def get_captcha():
    email = request.form.get("email")
    letter = string.ascii_letters + string.digits
    captcha = "".join(random.sample(letter, 4))
    print("\n",captcha,"\n")
    if email:
        message = Message(
            subject='进修馆',
            recipients=['{}'.format(email)],
            body="【进修馆】\n验证码为{}，请妥善保管。".format(captcha)
        )
        mail.send(message)
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if captcha_model:
            captcha_model.captcha = captcha
            captcha_model.create_time = datetime.datetime.now()
            db.session.commit()
        else:
            captcha_model = EmailCaptchaModel(email=email, captcha=captcha)
            db.session.add(captcha_model)
            db.session.commit()
            # code:200 成功的请求
        return jsonify({"code": 200})
    else:
        # code:400  客户端错误
        return jsonify({"code": 400, "message":"请先传递邮箱"})
    return

