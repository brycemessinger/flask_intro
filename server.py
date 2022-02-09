"""Greeting Flask app."""

from flask import Flask, request

app = Flask(__name__)

AWESOMENESS = [
    'cool', 'amazing', 'talented']

DISSES = [
    'garbage', 'terrible', 'the_worst']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Start Here</title>
      </head>
      <body>
        <a href="/hello">Take me to the start</a>
      </body>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method='GET'>
          What's your name? <input type="text" name="person">
          What compliment would you like?<br>
          If you don't want a compliment, you can choose a diss instead.<br>
          <input type="radio" name="compliment" value="cool">Cool<br>
          <input type="radio" name="compliment" value="amazing">Amazing<br>
          <input type="radio" name="compliment" value="talented">Talented<br>
          <input type="radio" name="diss" value="garbage">Garbage<br>
          <input type="radio" name="diss" value="terrible">Terrible<br>
          <input type="radio" name="diss" value="the_worst">The Worst!<br>

          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")
    diss = request.args.get("diss")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}{diss}!
      </body>
    </html>
    """

@app.route('/diss')
def diss_user():
    """Get user by name."""

    player = request.args.get("person")
    diss = request.args.get("diss")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")