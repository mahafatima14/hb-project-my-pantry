"""Server for pantry app."""

from flask import Flask

app = Flask(__name__)


# Replace this with routes and view functions!


if __name__ == "__main__":
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0", debug=True)
