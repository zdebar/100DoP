from flask import Flask, render_template
import random
from datetime import datetime
import requests


app = Flask(__name__)



@app.route('/')
def home():
    year = datetime.now().year
    return render_template("index.html", year=year)


@app.route('/guess/<name>')
def guess_name(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_url = "https://api.agify.io?name=michael"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("index.html", name=name, gender=gender, age=age)


@app.route('/blog/<num>')
def blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    post_response = requests.get(blog_url)
    all_posts = post_response.json()
    return render_template("blog.html", posts = all_posts)




if __name__ == "__main__":
    app.run(debug=True)


