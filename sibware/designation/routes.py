from flask import Flask,render_template,request , flash, redirect ,url_for ,session, Blueprint
from sibware import db, bcrypt,mail
from flask_login import login_user, current_user, logout_user, login_required
from cdifflib import CSequenceMatcher 
import string
import os
from sibware.models import User
import datetime
from itsdangerous import URLSafeTimedSerializer, SignatureExpired ,BadTimeSignature
from sibware.config import Config
from flask_mail import Message
designation = Blueprint('designation', __name__)

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (getattr(form, field).label.text, error), 'error')
@designation.route("/designations", methods=['GET','POST'])
def desgnations():
    root=current_user.id+1400
    current_user.identity_number="adm"+ str(root)
    db.session.commit()
    return render_template('admin_panel.html',current_user=current_user)

