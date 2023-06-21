from wtforms import TextField ,TextAreaField, StringField, SubmitField,PasswordField,RadioField, ValidationError, IntegerField,FileField,DateField
from  flask_wtf import FlaskForm
from wtforms.validators import DataRequired ,Length , Email, EqualTo, ValidationError
from wtforms.fields.html5 import DateField


global types_of_content
types_of_content=[('notes','Notes'),('home work','Home work'),('test','Test'),('study points','Study points'),('assignment','Assignment'),('report','Report')]

class AddDownloadableleContent(FlaskForm):
    type_of_content=SelectField('Type of Content',choices=types_of_content)
    title= TextField('Title',[DataRequired()])
    week_of_study= IntegerField('Week number: Optional')
    topic_number= IntegerField('Topic number')
    topic= TextField('Topic')
    submission_deadline= DateField('Submission deadline if relevant')
    
    submit=SubmitField('Add content')
    