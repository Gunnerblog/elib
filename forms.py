from wtforms import Form, BooleanField, TextField, PasswordField, validators
from wtforms.validators import ValidationError

from models import User

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35), 
        validators.Regexp("^[a-zA-Z0-9._%-]+@[a-zA-Z0-9._%-]+\.[a-zA-Z]{2,6}$")])

    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match'),validators.Length(min=6, max=16)
    ])
    confirm = PasswordField('Repeat Password')

    def validate_username(self, field):
    	users = User.query.all()
        for user in users:
            if field.data == user.name:
                raise ValidationError('User with current username already exist')

    def validate_email(self, field):
        users = User.query.all()
        for user in users:
            if field.data == user.email:
                raise ValidationError('User with current email already exist')


class AuthForm(Form):  
    email = TextField('Email Address')
    password = PasswordField('Password')

    def validate_password(self, field):
        user = User.query.filter(User.password == self.password.data, User.email == self.email.data).first()
        if not user:
            raise ValidationError("User with this email and password not exist")