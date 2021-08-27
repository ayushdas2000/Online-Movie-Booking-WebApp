from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField

#getting validators class from wtforms module
from wtforms.validators import DataRequired, Length, Email, EqualTo

#Writing in brackets means it is inheriting from FlaskForm class
class signupform(FlaskForm):
    #adding a string field
    #first argument is the name of the field
    #we also give a list of validator classes that are some checks
    firstname = StringField('fname', validators=[DataRequired(), Length(min = 2, max = 250)])
    firstname = StringField('lname', validators=[DataRequired(), Length(min = 2, max = 250)])
    email = StringField('emal', validators=[DataRequired(), Email()])
    mobilenum = StringField('mnum', validators=[DataRequired(), Length(min = 10, max = 12)])
    password = PasswordField('pword', validators=[DataRequired(), Length(min = 8, max = 300)])
    confpassword = PasswordField('cpword', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Signup')

class loginform(FlaskForm):
    email = StringField('emal', validators=[DataRequired(), Email()])
    password = PasswordField('pword', validators=[DataRequired(), Length(min = 8, max = 300)])
    remember = BooleanField('Rememberme')
    submit = SubmitField('login')
