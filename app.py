from flask import Flask, render_template, request, url_for, redirect
import secrets
from sqlalchemy import create_engine, MetaData, select
from sqlalchemy.orm import Session

from .lib.Forms import SignUpForm, LoginForm, DateForm

app = Flask(__name__)
secret = secrets.token_urlsafe(32)
app.secret_key = secret

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
        pass
    return render_template("SignUp.html", form=form)

@app.route("/Login", methods = ["GET", "POST"])
def Login():
    form = LoginForm()
    if request.method == "POST":
        #check against DB, if good, send back to homepage with user variable
        user = form.userName.data
        password = form.password.data
        print(user, password)
        return redirect(url_for("Home", user=user))
    return render_template("Login.html", form=form)



if __name__ == "__main__":
    app.run()
#this is a test attempt at pushing from the browser of my ipad
