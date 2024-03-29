# IMPORTS
from flask import Flask, abort
from markupsafe import escape

# FLASK
app = Flask(__name__) # create flask app instance

@app.route('/') # decorator
@app.route('/index/') # secondary route
def hello():
    return '<h1>Hello World!</h1>'

@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'

@app.route('/capitalize/<word>') # takes text and pass it to view function
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)

@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)