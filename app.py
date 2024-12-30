from flask import Flask, flash, render_template, request
from helpers import wordlist

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/play", methods=["GET", "POST"])
def play():
    
    if request.method == "GET":
        letters = ""
        word_dict = wordlist()
        word = str(word_dict['shavian'])
        english = str(word_dict['english'])
        masked = ""
        length = len(word)
        for char in word:
            masked += "_"
        return render_template("play.html", length=length, masked=masked, word=word, english=english)

    else:
        guess = request.form.get("guess")
        word = request.form.get("word") 
        letter = request.form.get("button")
        length = int(request.form.get("length"))
        masked = request.form.get("masked")
        english = request.form.get("english")
        letters = request.form.get("letters")

        if letter and letter not in word:
            letters = letters + letter + ','
        print(letter)
        print(letters)

        for i in range(length):
            if letter == word[i]:
                masked = masked[:i] + word[i] + masked[i + 1:]

        
        win = 0
        if word == masked or english == guess:
            masked = word
            win = 1

        if win == True:
            print("victory!")
        return render_template("play.html", length=length, letter=letter, letters=letters, masked=masked, word=word, english=english, win=win)


@app.route("/english", methods=["GET", "POST"])
def english():
    
    if request.method == "GET":
        letters = ""
        word_dict = wordlist()
        word = str(word_dict['english'])
        masked = ""
        length = len(word)
        for char in word:
            masked += "_"
        return render_template("english.html", length=length, masked=masked, word=word)

    else:
        guess = request.form.get("guess")
        word = request.form.get("word") 
        letter = request.form.get("button")
        length = int(request.form.get("length"))
        masked = request.form.get("masked")
        letters = request.form.get("letters")

        if letter and letter not in word:
            letters = letters + letter + ','
        print(letter)
        print(letters)

        for i in range(length):
            if letter == word[i]:
                masked = masked[:i] + word[i] + masked[i + 1:]

        
        win = 0
        if word == masked or word == guess:
            masked = word
            win = 1

        if win == True:
            print("victory!")
        return render_template("english.html", length=length, letter=letter, letters=letters, masked=masked, word=word, win=win)
