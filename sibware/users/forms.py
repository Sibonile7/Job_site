from wtforms import TextField ,TextAreaField, StringField, SubmitField,PasswordField,RadioField, ValidationError, IntegerField
from  flask_wtf import FlaskForm
from wtforms.validators import DataRequired ,Length , Email, EqualTo, ValidationError
from wtforms.fields.html5 import DateField

class RegForm(FlaskForm):
    
    firstname= TextField('First Name:' ,[ Length(min=2,max=80)])
    surname= TextField('Surname:' ,[ DataRequired(), Length(min=2,max=80)])
    second_name= TextField('Second name')
    phone_number= TextField('Phone number',[ DataRequired(), Length (min=4, max=15)])
    password=PasswordField('Password:',[ DataRequired(),Length(min=6,max=40)])
    confirm_password=PasswordField('Confirm Password:',[DataRequired(),Length(min=2,max=40),EqualTo('password',message='Passwords must match')])
    dob = DateField('Your date of birth', validators=[DataRequired()])
    gender= RadioField('Gender: ', choices=[('female','Female'),('male','Male')] )
    email= TextField('Email address optional')
    physical_address=TextAreaField('Address Where you live', [DataRequired(),Length(min=1, max=160)])
    submit =SubmitField('Register')
    
    
    
class LogForm(FlaskForm):
    email_address=TextField('Email address',[DataRequired(), Length(min=1, max=79)])
    password = PasswordField('Password:',[DataRequired()])
    submit= SubmitField('Login')
    