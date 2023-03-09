import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI_TEST')
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db' 
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('GM_USER')
    MAIL_PASSWORD = os.environ.get('GM_PASS')
    TESTING= True
