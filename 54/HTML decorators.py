from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


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