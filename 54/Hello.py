from flask import Flask

app = Flask(__name__)

class User:
    def __init__(self, name) -> None:
        self.name = name
        self.is_logged_in = False

@app.route("/")
def hello_world():
    return "<h1>Hello, World!<h1/>"


@app.route("/bye")
@make_bold
def bye():
    return "Bye!"


# Variabilní název cesty
@app.route("/<name>")
def greet(name):
    return f"Hello {name}"


if __name__=="__main__":
    app.run(debug=True)