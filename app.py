from flask import Flask, flash, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/play")
def play():
    return render_template("play.html")



@app.route("/wordbank", methods=["GET", "POST"])
def wordbank():

    return render_template("wordbank.html")
