from flask import Flask,render_template,request , flash, redirect ,url_for ,session, Blueprint, send_file, jsonify, make_response,send_file,current_app
from sibware import db, bcrypt,mail
from sibware.ranking.utils import savep, checker
from sqlalchemy import or_
from flask_login import login_user, current_user, logout_user, login_required
from  sibware.users.forms import RegForm,LogForm
from sibware.models import User,Chat,Messages
import datetime
from sqlalchemy import desc
from itsdangerous import URLSafeTimedSerializer, SignatureExpired ,BadTimeSignature
from sibware.config import Config
import random
import string
import os
from flask_mail import Message
users = Blueprint('users', __name__)

s= URLSafeTimedSerializer('NimNam%6678*8*#rt5%%isawinnerandavictor65')  

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (getattr(form, field).label.text, error), 'error')


@users.route("/", methods=['GET','POST'])
def home():
    if current_user.is_authenticated:
        if current_user.status==2:
            return redirect(url_for('users.user_login'))
        else:
            return redirect(url_for('users.admin_login'))
        
    form= LogForm()
    if form.validate_on_submit():
        email_address= form.email_address.data
        user= User.query.filter_by(email_address=email_address).first()
        if user is None:
            return '<h1>User not found</h1>'
        if user.status==2:
             if user and bcrypt.check_password_hash(user.password,form.password.data):
                 user.authenticated= True
                 login_user(user, remember= True)
                 return redirect(url_for('users.user_login'))
             else:
                flash_errors(form)
                flash('Login credentials are wrong')
                return render_template('base.html',form=form)
        else:    
            if user and bcrypt.check_password_hash(user.password,form.password.data):
                user.authenticated= True
                login_user(user, remember= True)
                return redirect(url_for('users.admin_login'))
            else:
                flash_errors(form)
                flash('Login credentials are wrong')
                return render_template('base.html',form=form)                
                            
    else:
        flash_errors(form)
        return render_template('base.html',form=form)
    return render_template('base.html',form=form)
   
@users.route('/user_register', methods=['GET', 'POST']) # student registration
def user_register():
    form= RegForm()
    if form.validate_on_submit():
        doby= request.form['dob']
        dob=datetime.datetime.strptime(doby, '%Y-%m-%d')
        x=datetime.datetime.now()
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        first_name=form.firstname.data
        surname=form.surname.data
        user=User(email_address=form.email.data,first_name=first_name,second_name=form.second_name.data,phone_number=form.phone_number.data,surname=surname,password=hashed_password,gender=form.gender.data ,date_of_birth=dob,date_time_of_join=x,status=2,physical_address=form.physical_address.data, type='unconfirmed',profile_pic="empty.PNG",title='user')
        db.session.add(user)
        db.session.commit()
        user.authenticated= True
        login_user(user, remember= True)
        return redirect (url_for('users.user_login'))
        
        
    else:
        flash_errors(form)
        render_template('registration.html',form=form)
    return render_template('registration.html',form=form)


    return render_template('school_admin_registration.html',form=form)
	
@users.route('/user_login', methods=['GET', 'POST'])
def user_login():
    return render_template('users_main.html',current_user=current_user)

@users.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    users=User.query.all()
    return render_template('admin_main.html',current_user=current_user,users=users)
 
@users.route('/see_user/<user_id>',methods=['GET','POST'])
def see_user(user_id):
    user=User.query.filter_by(id=user_id).first()
    return render_template('see_user.html',user=user)
    
@users.route('/user_profile',methods=['GET','POST'])
def user_profile():
    if current_user.status==2:
        return render_template('user_profile.html',current_user=current_user)
    else:
        return render_template('admin_profile.html',current_user=current_user)
            
@users.route("/update_profile_picture",methods=['POST','GET']) 
def update_profile_picture():
    if request.method=='POST':
        x=datetime.datetime.now()
        dat =x.strftime("%Y-%m-%d, %H-%M-%S") # to add uniquenss to input file names in static folder
        unik91=dat+ str(current_user.id) +''.join([random.choice(string.ascii_letters + string.digits) for n in range (7)])    
        profile_picture=savep(request.files['profile_pic'],unik91)
        user=User.query.filter_by(id=current_user.id).first()
        user.profile_pic=profile_picture
        current_user.profile_pic=profile_picture
        db.session.commit()
        if current_user.status==2:
            return redirect(url_for('users.user_login'))
        else:
            return redirect(url_for('users.admin_login'))

@users.route('/messaging',methods= ['GET','POST'])
def messaging():
    contacts=User.query.filter(User.id!=current_user.id).all()
    return render_template('admin_messages.html',current_user=current_user,contacts=contacts)
    
@users.route('/chat/<user_id>',methods= ['GET','POST'])
def chat(user_id):
    recipient=User.query.filter_by(id=user_id).first()
    incoming_messages=Messages.query.join(User,User.id==Messages.sender_id).filter(Messages.sender_id==user_id).filter(Messages.recipient_id==current_user.id).add_columns(User.first_name,User.surname,Messages.text,Messages.time).all()
    sent_messages=Messages.query.join(User,User.id==Messages.sender_id).filter(Messages.sender_id==current_user.id).filter(Messages.recipient_id==user_id).add_columns(User.first_name,User.surname,Messages.text,Messages.time).all()
    chat=Chat.query.filter(or_(Chat.starter_id == current_user.id,Chat.recipient_id == current_user.id)).first()
    if chat:
        return render_template('chat.html',chat=chat,recipient=recipient,current_user=current_user,incoming_messages=incoming_messages,sent_messages=sent_messages)
    else:
        chat=Chat(starter_id=current_user.id,recipient_id=recipient.id)
        db.session.add(chat)
        db.session.commit()
        return render_template('chat.html',current_user=current_user,chat=chat,recipient=recipient,messages=messages)
@login_required    
@users.route('/send_message',methods=['GET','POST'])
def send_message():
    if request.method=='POST':
        text=request.form['text']
        chat_idy=request.form['chat_idy']
        recipient_id=request.form['recipient_id']
        message=Messages(chat_idy=chat_idy,text=text,time=datetime.datetime.now(),sender_id=current_user.id,recipient_id=recipient_id)
        db.session.add(message)
        db.session.commit()
        return jsonify(success=True)
        
@users.route('/logout',methods= ['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('users.home'))