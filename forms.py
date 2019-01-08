from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired('Please enter your first name.')])
    last_name = StringField('Last Name', validators=[DataRequired('Please enter your last name.')])
    username = StringField('Username', validators=[DataRequired('Please enter a username.')])
    email = StringField('Email', validators=[DataRequired('Please enter your email.'), Email('Please enter your email.')])
    password = PasswordField('Password', validators=[DataRequired('Please enter a password.'), Length(min=6, message='Passwords must be larger than 6 characters.')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired('Please enter your email.'), Email('Please enter your email.')])
    password = PasswordField('Password', validators=[DataRequired('Please enter a password.')])
    submit = SubmitField('Sign In')


class TransferForm(FlaskForm):
    receiver_email = StringField('Receiver Email', validators=[DataRequired('Please enter an email.'), Email('Please enter the email of the reciever.')])
    amount = FloatField('Amount', validators=[DataRequired('Please enter the amount to send.')])
    submit = SubmitField('Transfer Money')