from wtforms import TextField ,TextAreaField, StringField, SubmitField,PasswordField,RadioField, ValidationError, IntegerField
from  flask_wtf import FlaskForm
from wtforms.validators import DataRequired ,Length , Email, EqualTo, ValidationError
from wtforms.fields.html5 import DateField

class PostForm(FlaskForm):
     title= TextField('Title:' ,[ DataRequired(),Length(min=2,max=80)])
     content=TextAreaField('Type in')
     submit=SubmitField('Post')

class RegForm1(FlaskForm):
    firstname= TextField('First Name:' ,[ Length(min=2,max=80)])
    surname= TextField('Surname:' ,[ DataRequired(), Length(min=2,max=80)])
    second_name= TextField('Second name')
    phone_number= TextField('Parents phone number',[ DataRequired(), Length (min=4, max=15)])
    password=PasswordField('Password:',[ DataRequired(),Length(min=6,max=40)])
    confirm_password=PasswordField('Confirm Password:',[DataRequired(),Length(min=2,max=40),EqualTo('password',message='Passwords must match')])
    dob = DateField('Your date of birth', validators=[DataRequired()])
    gender= RadioField('The teacher is ', choices=[('female','Woman'),('male','Man')] )
    email= TextField("Teacher's email address", [DataRequired()])
    physical_address=TextAreaField('Address Where you live', [DataRequired(),Length(min=1, max=160)])
    title= TextField('Title Mr/Mrs ',[DataRequired()])
    submit =SubmitField('Add Teacher')
    
class SearchText(FlaskForm):
    text=TextField('Search',[DataRequired(), Length(min=1, max=700)], description="image link  or product name")
    submit=SubmitField('Search User')
    
class Add_teacherForm(FlaskForm):
    title=TextField('Title Mr Mrs',[DataRequired(), Length(min=2,max=4)])
    first_name=TextField('First name',[DataRequired(),Length(min=2,max=80)])
    surname= TextField('Surname', [DataRequired()])
    email= TextField('Email ',[DataRequired(),Email('Enter a valid email adress')])
    subject_id=IntegerField('subject_id',[DataRequired()])
    
    submit=SubmitField('Add Teacher')
    
class AddClassForm(FlaskForm):
    class_name=TextField('Class identity', [DataRequired()])
    stream= TextField('Stream',[DataRequired()])
    class_teacher= TextField('Class teacher', [DataRequired()])
    submit=SubmitField('Add Class')
      
    
    