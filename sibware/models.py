from sibware import db,login_manager
from flask_login import  UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Tables Start Now

class User(db.Model,UserMixin):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key= True)
    email_address = db.Column(db.String(120))
    first_name= db.Column(db.String(80),nullable= False)
    second_name=db.Column(db.String(80),nullable= True)
    phone_number=db.Column(db.String(20),nullable= False)
    surname= db.Column(db.String(80),nullable= False)
    password= db.Column(db.String(260),nullable=False)
    gender= db.Column(db.String(80),nullable=False)
    date_of_birth= db.Column(db.DateTime,nullable= False)
    date_time_of_join= db.Column(db.DateTime,nullable= False)
    status=db.Column(db.Integer,nullable= False)
    profile_pic= db.Column(db.String(260))
    security_qstn= db.Column(db.String(160))
    security_answer= db.Column(db.String(160))
    physical_address=db.Column(db.String(180))
    type= db.Column(db.String(80),nullable= False)
    name_of_school=db.Column(db.String(80))
    identity_number=db.Column(db.String(80))
    top_clearance=db.Column(db.Boolean)
    title=db.Column(db.String(50))
    activation=db.Column(db.Boolean)
    
    activities=db.relationship('Activitylog',backref='user_id',lazy= True)
    def __init__self(self,email_address,first_name,surname,password ,gender,date_of_birth,date_time_of_join,status,type):
        self.email_address = email_address
        self.firstname= firstname
        self.surname= surname
        self.password= password
        self.gender= gender
        self.date_of_birth= date_of_birth
        self.date_time_of_join= date_time_of_join
        self.status= status
        self.type= type
        
    def __repr__(self):
        return '<User %r>' % self.id

class Chat(db.Model):
    __tablename__='chat'
    id=db.Column(db.Integer,primary_key= True)
    starter_id=db.Column(db.Integer,nullable =False)
    recipient_id=db.Column(db.Integer,nullable =False)
    messages=db.relationship('Messages',backref='user_id',lazy=True)
    
    def __init__self(self,starter_id,recipient_id):
        self.starter_id=starter_id
        self.recipient_id=recipient_id
        
class Messages(db.Model):
    __tablename__='messages'
    id=db.Column(db.Integer,primary_key= True)
    chat_idy=db.Column(db.Integer,db.ForeignKey('chat.id'),nullable= False)
    text=db.Column(db.Text)
    time=db.Column(db.DateTime)
    sender_id=db.Column(db.Integer,nullable =False)
    static_file=db.Column(db.String(360))
    recipient_id=db.Column(db.Integer,nullable=False)
    seen=db.Column(db.Boolean)
    
    def __init__self(self,chat_idy,text,time,sender_id,recipient_id,seen):
        self.chat_idy=chat_idy
        self.text=text
        self.time=time
        self.sender_id=sender_id
        
    
        
    
class Activitylog(db.Model):
    __tablename__='activitylog'
    id=db.Column(db.Integer,primary_key= True)
    user_idy= db.Column(db.Integer,db.ForeignKey('user.id'),nullable= False)
    activity_date= db.Column(db.DateTime)
    action= db.Column(db.String(700))
    
    def __init__self(user_idy,activity_date,action):
        self.user_idy= user_idy
        self.activity_date= activity_date
        self.action= action
        

        
    
        
    
        
    
    

