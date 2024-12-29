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
        length = len(word)
        for char in word:
            masked += "_"
        return render_template("play.html", length=length, masked=masked, word=word)

    else:
        word = request.form.get("word") 
        letter = request.form.get("button")
        length = int(request.form.get("length"))
        masked = request.form.get("masked")



        for i in range(length):
            if letter == word[i]:
                masked = masked[:i] + word[i] + masked[i + 1:]
        
        return render_template("play.html", length=length, letter=letter, masked=masked, word=word)



@app.route("/wordbank", methods=["GET", "POST"])
def wordbank():
    return render_template("wordbank.html")
