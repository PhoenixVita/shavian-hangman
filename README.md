# shavian-hangman
#### Video Demo: https://www.youtube.com/watch?v=0j8gmCEkLAg
#### Description:
Hi, decided to create a web app for CS50's final project using Python and the Flask web framework.

Shavian Hangman is an idea I came up with since I was learning Shavian at the time and wanted to see what it would be like to play hangman, but with Shavian words! Admittedly, the experience was worse than I expected, which is why I added an English alphabet version as well to compensate for the time I spent making this (way too long)

##### index
Lets start off with the index page. First, I filled out the usual boilerplate then I added my lil stick figure image and 3 buttons. Later on I decided to use Jinja to create a template which I could extend from, that being layout.html. Originally the 2nd button was to redirect the user to a page where they could input their own words, but I saw that as unnecessary and changed it to being an EN (english alphabet) version of my hangman game instead.

##### app
So here is where all the behind the scene magic happens. On the /play page, the first thing that happens is the function checks to see if the request method is GET, then I initialize a few variables, grab a random Shavian word from a list of dicts that I'm storing in a helper file within a function that I called. I also create an English copy of the word by accessing the other key value pair in the randomly chosen word I got from my function. A copy of the Shavian word is made, with each character being replaced with an underscore, and the POST section replaces it with the actual character whenever the user submits a form and the letter matches what it is in the index that its in in the original copy of the word. 
This next part took forever, I had to figure out how to carry data from the GET section of my function over to POST. I tried using sessions at first but for some reason it wouldn't work no matter what solution I looked at online, then I learned about something that fields that I could have in my html file that I pull the request from which worked perfectly.
I have a few conditionals and loop that work to correctly display the string on the page as well as wrong answers that the user inputs. 
One thing that annoyed me for half an hour was figuring out how to go to an index in a string and replace a char since it wouldn't work like how Id've done it in C, but eventually I found a method.
The win and lose conditionals just check to see if the original word is equal to the masked (after the reveal) or if the user's guess is correct, to which I display a block of code on play.html that essentially says "hey, you won!", and vice versa for if the user loses.

For the english function is pretty self explainable. I did all the same thing as the play function but with just the english key value pair instead, substituting "word" in the play function. There probably was a better way to implement this, but I just copy and pasted everything.

##### play.html and english.html
The masked word, length of the word, and wrong letters inputted by the user in this section is sent to app.py via POST and is returned back here to which it is displayed at the top of the screen.
I have several buttons with values which are what get sent to the back end. 
Two conditions for win and lose, which how they work I explained in the app section above. The rest is pretty self explainatory.

##### database
I accessed the words from TSV available here: https://github.com/Shavian-info/readlex
and compared them to another CSV that's for a list of commonly used hangman words in English.
The query I used is available in query.sql and all the tables and their respective data are in shavian.db

##### helpers
I made a simple function that grabs a random dict from the list, but the list itself I had ChatGPT help me out by converting text from my SQL query into that syntax thats usable for lists in Python.

##### stylesheet.css
Just some styles for the site. It should support mobile as well. For the color scheme I tried to follow Catppuccin Frappé which you can find here: https://catppuccin.com/palette
I did not use bootstrap, all the styling are written by myself.

##### main.js 
Just some simple event listener functions that I used to give a lil life to my index page. When the user hovers their mouse over a button, it turns to a color which goes away once the mouse is no longer on the button.