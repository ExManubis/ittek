# IMPORTS
import base64
from io import BytesIO
from matplotlib.figure import Figure
from flask import Flask, render_template
from get_stue_dht11_data import get_stue_data
import paho.mqtt.publish as publish

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
    ax.tick_params(axis='x', colors='blue') # timestamp text color
    ax.set_facecolor('#111') # indre ramme farve
    ax.plot(timestamps, temp, linestyle = 'dashed', c='#11f', linewidth='1.5', marker='o', mec='red', ms=10, mfc='yellow')
    ax.set_xlabel('Timestamps')
    ax.set_ylabel('Temperature C')
    ax.spines['left'].set_color('blue')
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
    fig.subplots_adjust(bottom=0.3)
    ax.tick_params(axis='x', which='both', rotation=30)
    ax.tick_params(axis='x', colors='blue') # timestamp text color
    ax.set_facecolor('#111') # indre ramme farve
    ax.plot(timestamps, hum, linestyle = 'dashed', c='#11f', linewidth='1.5', marker='o', mec='red', ms=10, mfc='yellow')
    ax.set_xlabel('Timestamps')
    ax.set_ylabel('Humidity')
    ax.spines['left'].set_color('blue')
    fig.patch.set_facecolor('#234')
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

@app.route('/koekken')
def koekken():
    return render_template('koekken.html')

@app.route('/taend', methods=['POST'])
def taend():
    publish.single("LED", "taend", hostname="20.13.128.184")
    return render_template('koekken.html')

@app.route('/sluk', methods=['POST'])
def sluk():
    publish.single("LED", "sluk", hostname="20.13.128.184")
    return render_template('koekken.html')

# SCRIPT
app.run(debug=True)