from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username=StringField('Username', 
                        validators=[DataRequired(),Length(min=2,max=20)])

    email=StringField('email',
                        validators=[DataRequired(), Email()])

    password=PasswordField('Password', validators=[DataRequired()])

    confirm_password=PasswordField('Confirm Password',
                        validators=[DataRequired(),EqualTo('password')])

    submit=SubmitField('Sign Up')

    # custom validations
    
    # Template:
    # def validate_field(self, field):
    #    if True:
    #        raise ValidationError('Validation Message')

    def validate_username(self, username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists.') 

    def validate_email(self, email):
        user=User.query.filter_by(email=email.data).first()    
        if user:
            raise ValidationError('Email already in use.') 

    

class LoginForm(FlaskForm):
    email=StringField('email',
                        validators=[DataRequired(), Email()])

    password=PasswordField('Password', validators=[DataRequired()])

    remember=BooleanField('Remember Me')

    submit=SubmitField('Login')
