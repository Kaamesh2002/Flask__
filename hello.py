from flask import Flask,render_template,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "kaamesh2002"


# create a form class
class NamerForm(FlaskForm):
    name = StringField("What is your name",validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/')

def index1():
    # return "<h1>hello</h1>"
    return render_template("hello.html")

@app.route('/user/')

def index():
    first_name = 'john'
    stuff = 'this is <strong>bold</strong>'
    pizza = ['pepper','mayo', 41]
    flash("dummy")
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

@app.route('/name',methods=['GET','POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully")
    return render_template("name.html",name = name,form= form ) 