from flask import Flask, flash, render_template, request
from helpers import wordlist

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/play")
def play():
    
    word = wordlist()

    return render_template("play.html", word=word)



@app.route("/wordbank", methods=["GET", "POST"])
def wordbank():
    return render_template("wordbank.html")
