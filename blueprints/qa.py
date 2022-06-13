# -*- coding: utf-8 -*-
# @Time    : 2022/5/16 12:48
# @Author  : 张梓锐
# @File    : qa.py
# @Software: PyCharm 
# @Content : 问答进程相关

from flask import Blueprint,render_template, g, request, redirect, url_for, flash
from .forms import QuestionForm,AnswerForm
from models import Question_Model,AnswerModel
from extends import db
from decorators import login_required
from sqlalchemy import or_

bp = Blueprint("qa", __name__, url_prefix="/")


@bp.route('/')
# @login_required
def index():
    questions = Question_Model.query.order_by(db.text("-create_time")).all()
    return render_template("index.html", questions=questions)


@bp.route("/question/public", methods=['GET', 'POST'])
@login_required
def public_question():
    # 判断是否登录，如果没有登录，跳转到登录页面
    if request.method == 'GET':
        return render_template("public_question.html")
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            # print("\n", g.user.id,"\n","\n")
            question = Question_Model(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect("/")
        else:
            flash("标题或内容格式错误")
            return redirect(url_for("qa.public_question"))


@bp.route("/question/<int:question_id>")
def question_detail(question_id):
    question = Question_Model.query.get(question_id)
    return render_template("detail.html", question=question)


@bp.route('/answer/<int:question_id>', methods=["POST"])
@login_required
def answer(question_id):
    form = AnswerForm(request.form)
    if form.validate():
        content = form.content.data
        answer_model = AnswerModel(content=content,author=g.user,question_id=question_id)
        db.session.add(answer_model)
        db.session.commit()
        return redirect(url_for("qa.question_detail",question_id=question_id))
    else:
        flash("评论失败") # 内含敏感词或者空评论
        return redirect(url_for("qa.question_detail",question_id=question_id))


@bp.route('/search')
def search():
    # /search?q=xxx
    q = request.args.get("q")
    # filter_by:直接使用字段名称
    # filter: 使用模型.字段名称
    questions = Question_Model.query.filter(or_(Question_Model.title.contains(q),Question_Model.content.contains(q))).order_by(db.text("-create_time"))
    return render_template("index.html",questions=questions)