# IMPORTS
from flask import Flask, render_template

# CLASSES + OBJECTS
app = Flask(__name__) # instans af flask class

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/contact/')
def contact():
    return render_template("contact.html")