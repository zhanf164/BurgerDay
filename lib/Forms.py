from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, widgets, BooleanField
from wtforms.validators import DataRequired, Length, Email
# from wtforms.fields.html5 import EmailField
from wtforms.fields import EmailField
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
    submit = SubmitField("Submit")

class DateForm(FlaskForm):
    choices = [("first","October 1st-2nd"), ("second", "October 8th-9th"), ("third", "October 16th-17th"), ("fourth", "October 22nd-23rd"), ("fifth", "October 30th-31st")]
    first = BooleanField("October 1st-2nd")
    second = BooleanField("October 8th-9th")
    third = BooleanField("October 16th-17th")
    fourth = BooleanField("October 22nd-23rd")
    fifth = BooleanField("October 30th-31st")
    submit = SubmitField("Submit Choices")