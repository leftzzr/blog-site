# -*- coding: utf-8 -*-
# @Time    : 2022/5/17 9:38
# @Author  : 张梓锐
# @File    : forms.py
# @Software: PyCharm 
# @Content : 表单验证
from .user import EmailCaptchaModel, User_Model
import wtforms
from wtforms.validators import length, EqualTo, email,InputRequired


class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[email()])
    password = wtforms.StringField(validators=[length(min=6, max=20)])


class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=3, max=20)])
    email = wtforms.StringField(validators=[email()])
    captcha = wtforms.StringField(validators=[length(min=4, max=4)])
    password = wtforms.StringField(validators=[length(min=6, max=20)])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])

    def validate_captcha(self, field):
        captcha = field.data
        email_ = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email_).first()
        if not captcha_model or captcha_model.captcha.lower() != captcha.lower():
            # print(1)
            raise wtforms.ValidationError("邮箱验证码错误")

    def validate_email(self, field):
        email_ = field.data
        user_model = User_Model.query.filter_by(email=email_).first()
        if user_model:
            # print(2)
            raise wtforms.ValidationError("该邮箱已注册")


class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[length(min=2, max=100)])
    content = wtforms.StringField(validators=[length(min=5)])
    # 敏感词验证


class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[length(min=1)])
    # 敏感词
