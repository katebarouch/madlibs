"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


# @app.route("/hello")
# def say_hello():
#     """Say hello to user."""

#     return render_template("hello.html")


@app.route("/game")
def ask_question():
    """Greet user with question."""

    return render_template("compliment.html")

@app.route("/yesorno")
def show_madlib_form():
    """Show madlib form."""

    answer = request.args.get("answer")
    if answer == "yes": #Q on how to reference radio button
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route("/madlib")
def show_madlib():
    place = request.args.get("place")#how to reference and integrate into madlib template
    mythical_creature = request.args.get("mythical creature")
    noun = request.args.get("noun")
    adjective1 = request.args.get("adjective1")
    adjective2 = request.args.get("adjective2")
    adjective3 = request.args.get("adjective3")
    return render_template("madlib.html", place=place, mythical_creature = mythical_creature, noun=noun, adjective1=adjective1, adjective2=adjective2, adjective3=adjective3)

if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0", port="5001")
