from flask_wtf import FlaskForm
from flask_wtf.csrf import validate_csrf
from flask_wtf.recaptcha import validators
from wtforms import (
    StringField, 
    PasswordField, 
    EmailField, 
    DateField)
from wtforms.validators import DataRequired, Length, EqualTo, Email


class UserCreateForm(FlaskForm):
    username = StringField('ID', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('password (less then 5)', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다.'), Length(min=6)])
    password2 = PasswordField('password confirm', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])
    birth = DateField('birth date', validators=[DataRequired()])

class UserSigninForm(FlaskForm):
    username = StringField('ID', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired()])