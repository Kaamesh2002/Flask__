from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

def index1():
    return "<h1>hello</h1>"

@app.route('/user/')

def index():
    first_name = 'john'
    stuff = 'this is <strong>bold</strong>'
    pizza = ['pepper','mayo', 41]
    return render_template("index.html", first_name = first_name,stuff = stuff,favourite_pizza = pizza)

@app.route('/user/<name>')

def user(name):
    # return "<h1>Hello {}</h1>".format(name)
    return render_template("user.html", user_name = name)

# 404 server error
@app.errorhandler(404)

def page_not_found(e):
    return render_template("404.html"),404

# 500 internal server error
@app.errorhandler(500)

def page_not_found(e):
    return render_template("500.html"),500


