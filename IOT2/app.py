# IMPORTS
from flask import Flask, render_template

# FLASK APP
app = Flask(__name__)

# FLASK ROUTES
## Home
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/stue')
def stue():
    return render_template('stue.html')

# SCRIPT
app.run(debug=True)