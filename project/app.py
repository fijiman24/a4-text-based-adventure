"""This is the main Flask application file. It imports the game logic from
the simple_game.py file and uses it to update the game state. It also handles user
input and displays the game state in the browser.

Rename to app.py to run.
"""

from flask import Flask, render_template, request
from simple_game import game

app = Flask(__name__)


@app.route("/")
def index():
    """
    This is the main route of the application. It calls the game function to
    get the initial game state and displays it in the browser.
    """
    curr_coords, goal_corrds, error_message, game_over = game()
    return render_template(
        "index.html",
        curr_coords=curr_coords,
        goal_corrds=goal_corrds,
        error_message=error_message,
        game_over=game_over,
    )


@app.route("/move", methods=["POST"])
def move():
    """
    This route handles user input. It calls the game function with the
    user's input and updates the game state. It then displays the updated
    game state in the browser.
    """
    direction = request.form["direction"]
    curr_coords, goal_corrds, error_message, game_over = game(direction)
    return render_template(
        "index.html",
        curr_coords=curr_coords,
        goal_corrds=goal_corrds,
        error_message=error_message,
        game_over=game_over,
    )


if __name__ == "__main__":
    """
    This is the main entry point of the application.
    It runs the Flask development server.
    """
    app.run(debug=True)
