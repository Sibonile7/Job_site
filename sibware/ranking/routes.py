from flask import Flask,render_template,request , flash, redirect ,url_for ,session, Blueprint,current_app, jsonify,make_response
from sibware import db, bcrypt,mail
from flask_login import login_user, current_user, logout_user, login_required
from sibware.models import User
from sibware.ranking.utils import savep, checker,save_downloadable
import datetime
from itsdangerous import URLSafeTimedSerializer, SignatureExpired ,BadTimeSignature
from sibware.config import Config
from flask_mail import Message
from sqlalchemy import desc
import sys
import os
import string
import random
import dumper
from operator import itemgetter
from werkzeug.utils import secure_filename
ranking = Blueprint('ranking', __name__)

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (getattr(form, field).label.text, error), 'error')
            
@ranking.route("/rank_jobs", methods=['GET','POST'])
def rank_jobs():
    if request.method=='POST':
        jobs=[]
        high_level_pl=['python','c++','c#','java','ruby','javascript','rust','php','go']
        low_level_pl=['assembly','arduino','algol']
        mabasa={'Systems Designer':8,'Full stack developer':6,'Front End developer':4,'Systems Analyst':9,'Natural Language processing partner':8,'Android app developer':5,'Cyber Security Analyst':7,'Ethical Hacker':8,'Software Tester':7,'Database Admin':7}
        degree_program=request.form['degree_program']
        occupations=request.form['occupation']
        user=User.query.filter_by(id=current_user.id).first()
        user.security_answer=degree_program
        db.session.commit()
        p_lge= request.form['pl']
        pl=p_lge.lower()
        if pl in high_level_pl:
            pl_grade=4
        elif pl in low_level_pl:
            pl_grade=2
        else:
            return"<h1> Enter a relavant programming language</h1>"
        if degree_program=='Computer Science' or degree_program=='Software Engineering':
            degree_grade=3
        elif degree_program=='Computer Engineering':
            degree_grade=4
        else:
            degree_grade=2
        overall_grade=degree_grade+pl_grade+ 1
        for key,value in mabasa.items():
            if value <=overall_grade:
                if [key,value] not in jobs:  #prevent duplication of results
                    jobs.append([key,value])
        jobs=sorted(jobs, key=itemgetter(1),reverse=True)
        return render_template('rank_page.html',current_user=current_user,jobs=jobs,overall_grade=overall_grade)