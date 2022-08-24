from flask import Flask, render_template, request, url_for, redirect
import secrets
from sqlalchemy import create_engine, MetaData, select
from sqlalchemy.orm import Session

from .lib.Forms import SignUpForm, LoginForm, DateForm
from .lib.DBOperations import *

app = Flask(__name__)
secret = secrets.token_urlsafe(32)
app.secret_key = secret

DB_CONNECTION_STRING = ""


@app.route("/", methods = ["GET", "POST"])
@app.route("/Home", methods=["GET", "POST"])
@app.route("/Home/<user>", methods=["GET", "POST"])
def Home(user=None):
    form = DateForm()
    #fetch current preferences from database if logged in so we can display them if they exist
    if user != None:
        #fetch preferences here
        preferences = "These Dates"
    else:
        preferences=None
    
    if request.method == "POST":
        if user == None:
            return redirect(url_for("Login"))
        else:
            choice1 = form.first.data
            choice2 = form.second.data
            choice3 = form.third.data
            choice4 = form.fourth.data
            choice5 = form.fifth.data
            return render_template("Homepage.html", form=form, user=user, preferences=preferences)
    return render_template("HomePage.html", form=form, user=user)


@app.route("/SignUp", methods=["GET", "POST"])
def SignUp():
    form = SignUpForm()
    if request.method == "POST":
        firstName = form.firstName.data
        lastName =  form.lastName.data
        email = form.email.data
        userName = form.email.data
        passWord = form.passWord.data
        InsertUser(firstName, lastName, email, userName, passWord)
        return url_for("Home", user=user)
    return render_template("SignUp.html", form=form)

@app.route("/Login", methods = ["GET", "POST"])
def Login(message=None):
    form = LoginForm()
    if request.method == "POST":
        #check against DB, if good, send back to homepage with user variable
        user = form.userName.data
        password = form.password.data
        exists = AuthenticateUser(user, password)
        if exists:
            return redirect(url_for("Home", user=user))
        else:
            return redirect(url_for("Login"), form=form, message="Invalid Credentials")
    return render_template("Login.html", form=form)



if __name__ == "__main__":
    app.run()
