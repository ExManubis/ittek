# IMPORTS
from flask import Flask, render_template

# FLASK
## Flask app
app = Flask(__name__)

## Flask routes
@app.route('/')
def home():
    return render_template('index.html')

# SCRIPT
app.run(debug=True) # runs with debug