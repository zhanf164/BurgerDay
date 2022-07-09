from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/Home")
def Home():
    return render_template("HomePage.html")


@app.route("/SignUp")
def SignUp():
    return render_tempate("SignUp.html")

@app.route("/Login", methods = ["GET", "POST"])
def Login():
    if request.method == "POST":
        print("request was made")
    return render_template("Login.html")



if __name__ == "__main__":
    app.run()
