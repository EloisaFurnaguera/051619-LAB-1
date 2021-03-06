"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = ["ugly", "tonta", "pesada"]    


@app.route("/")
def start_here():
    """Home page."""

    return """<!doctype html>
                  <html>
                  <body>
                  <p>Hi! This is the home page.</p>
                  <a href = "/hello">Do you want to go to hello</a>
                  </body>
                  </html>"""


@app.route("/hello")
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
        <form action="/greet">
          What's your name? <input type="text" name="person"><br>
          Pick a complement
          <select name = "complement">
          <option value = "awesome">awesome</option>
          <option value = "terrific">terrific</option>
          <option value = "neato">neato</option>
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("complement")

  
    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!<br>
        <a href="/diss?person={}">Do you want to hear the truth?</a>
      </body>
    </html>
    """.format(player, compliment, player)


@app.route("/diss")
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    insults = choice(INSULTS)

  
    return """
    <!doctype html>
    <html>
      <head>
        <title>Insults</title>
      </head>
      <body>
         {}! you're {}!
      </body>
    </html>
    """.format(player, insults)







if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
