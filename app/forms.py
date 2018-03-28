from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8, max=25, message='please use a stronger password')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login now')

class Registration(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Password', validators=[DataRequired(), EqualTo('password)')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter(username=username.data).first()
        if user is not None:
            raise ValidationError('This username is not available')

    def validate_email(self, email):
        email = User.query.filter(email=email.data).first()
        if email is not None:
            raise ValidationError('This email is already in use')
    