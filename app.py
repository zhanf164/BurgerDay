from flask import Flask, render_template, request

@route("/")
@route("/Home")
def Home():
    return render_template("HomePage.html")


@route("/Login", methods = ["GET", "POST"])
def Login():
    if request.method == "POST":
        print("request was made")
    return render_template("Login.html")



if __name__ == "__main__":
    app = Flask(__name__)
