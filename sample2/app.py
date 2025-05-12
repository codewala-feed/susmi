from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homePage():
    return render_template("index.html")

@app.route("/wish", methods=["GET"])
def wishUser():
    return "Happy Coding :)" 