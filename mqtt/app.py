# IMPORTS
import base64
from io import BytesIO
from flask import Flask, render_template
from matplotlib.figure import Figure
from get_kontor_dht11_data import get_kontor_data

# FLASK
## Flask app
app = Flask(__name__)

## Flask routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/kontor')
def kontor():
    kontor_temperature = kontor_temp()
    kontor_humidity = kontor_hum()
    print(kontor_temperature)
    print(kontor_humidity)
    return render_template('kontor.html', kontor_temperature = kontor_temperature, kontor_humidity = kontor_humidity) 

# FUNCTIONS
def kontor_temp():
    timestamps, temp, hum = get_kontor_data(10)

    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot(timestamps, temp)
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

def kontor_hum():
    timestamps, temp, hum = get_kontor_data(10)

    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot(timestamps, hum)
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

# SCRIPT
app.run(debug=True) # runs with debug