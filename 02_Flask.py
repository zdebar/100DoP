from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Ahoj"

#__name__ Jméno modulu


