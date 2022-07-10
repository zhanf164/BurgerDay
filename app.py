from flask import Flask, render_template, request, url_for
import secrets

from .lib.Forms import SignUpForm, LoginForm, DateForm

app = Flask(__name__)
secret = secrets.token_urlsafe(32)
app.secret_key = secret

@app.route("/", methods = ["GET", "POST"])
@app.route("/Home", methods=["GET", "POST"])
def Home():
    form = DateForm()
    return render_template("HomePage.html", form=form)


@app.route("/SignUp", methods=["GET", "POST"])
def SignUp():
    form = SignUpForm()
    if request.method == "POST":
        pass
    return render_template("SignUp.html", form=form)

@app.route("/Login", methods = ["GET", "POST"])
def Login():
    if request.method == "POST":
        print("request was made")
    return render_template("Login.html")



if __name__ == "__main__":
    app.run()
