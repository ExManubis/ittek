# IMPORTS
import base64
from io import BytesIO
from matplotlib.figure import Figure
from flask import Flask, render_template
from get_stue_dht11_data import get_stue_data

# FLASK APP
app = Flask(__name__)

# FUNCTIONS
def stue_temp():
    timestamps, temp, hum = get_stue_data(10) # Unpack data
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    fig.subplots_adjust(bottom=0.3)
    ax.tick_params(axis='x', which='both', rotation=30)
    ax.set_facecolor('#111') # indre ramme farve
    ax.plot(timestamps, temp, linestyle = 'dashed', c='#11f', linewidth='1.5', marker='o', mec='red', ms=10, mfc='yellow')
    ax.set_xlabel('Timestamps')
    ax.set_ylabel('Temperature C')
    fig.patch.set_facecolor('#234')
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

def stue_hum():
    timestamps, temp, hum = get_stue_data(10) # Unpack data
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

# FLASK ROUTES
## Home
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/stue')
def stue():
    stue_temperature = stue_temp()
    stue_humidity = stue_hum()
    return render_template('stue.html', stue_temperature = stue_temperature, stue_humidity = stue_humidity)

# SCRIPT
app.run(debug=True)