from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, widgets, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email
from wtforms.fields.html5 import EmailField
import email_validator

class SignUpForm(FlaskForm):
    firstName = StringField("firstName", validators=[DataRequired()])
    lastName = StringField("lastName", validators=[DataRequired()])
    email = EmailField("email", validators=[DataRequired(), Email()])
    userName = StringField("userName", validators=[DataRequired()])
    passWord = StringField("password", validators=[DataRequired(), Length(min=8, max=80)], widget=widgets.PasswordInput(hide_value=True))
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    userName = StringField("username", validators=[DataRequired()])
    password = StringField("password", validators=[DataRequired()], widget=widgets.PasswordInput(hide_value=True))

class DateForm(FlaskForm):
    choices = ["October 1st-2nd", "October 8th-9th", "October 16th-17th", "October 22nd-23rd", "October 30th-31st"]
    dates = SelectMultipleField(choices=choices)
    submit = SubmitField("Submit Choices")