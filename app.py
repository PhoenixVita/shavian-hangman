from flask import Flask, flash, render_template, request
from helpers import wordlist

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/play", methods=["GET", "POST"])
def play():
    
    if request.method == "GET":
        word = str(wordlist())
        masked = ""
        length = strlen(word)
        for char in word:
            masked += "_ "
        return render_template("play.html",masked=masked)



@app.route("/wordbank", methods=["GET", "POST"])
def wordbank():
    return render_template("wordbank.html")
