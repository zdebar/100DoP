from flask import Flask
import random

app = Flask(__name__)



@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
            "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExamQ0cTAyd213OHZ1ZHp2cGM2MjZqdjhla3VzdHlnc2pyaXp5MWQ1YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oUmBwN6mihDY4/giphy.gif'>"

number = random.randint(1,10)

# Název proměnné
@app.route("/<int:guess>")
def test_number(guess):
    if guess == number:
        return f"That's it!"
    elif guess < number:
        return f"Too low!"
    else:
        return f"Too high!"


if __name__=="__main__":
    app.run(debug=True)



