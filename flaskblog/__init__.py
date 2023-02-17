import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY']='a343c940d73bd8707d351de0db9c6da6'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db= SQLAlchemy(app)
bcrypt=Bcrypt(app)

login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']=os.environ.get('GM_USER')
app.config['MAIL_PASSWORD']=os.environ.get('GM_PASS')
mail=Mail(app)

from flaskblog import routes # need to avoid circular import problems
