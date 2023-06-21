from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail,Message
from sibware.config import Config

db = SQLAlchemy()
bcrypt= Bcrypt()
login_manager=LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail =Mail()

def create_app(config_class=Config):
    app= Flask(__name__)
    with app.app_context():# we may  use  the application with context because of our python models 
        app.config.from_object(Config)
    
        db.init_app(app)#not your conventional db = SQLAlchemy(app)
        bcrypt.init_app(app)
        login_manager.init_app(app)#app initializations
        mail.init_app(app)
        #importing blueprints to the initializing module
        from sibware.designation.routes import designation
        from sibware.ranking.routes import ranking
        from sibware.users.routes import users
        
        #Registering blueprints 
        app.register_blueprint(ranking)
        app.register_blueprint(designation)
        app.register_blueprint(users)

    return app
    