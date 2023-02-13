from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_loing import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY']='a343c940d73bd8707d351de0db9c6da6'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db= SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)

from flaskblog import routes # need to avoid circular import problems
