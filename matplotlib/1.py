# IMPORTS
import base64
from io import BytesIO
from flask import Flask
from matplotlib.figure import Figure

# FLASK APP
app = Flask(__name__)

## FLASK ROUTES
@app.route('/')
def hello():
    # generate figure without using pyplot
    fig = Figure()
    ax = fig.subplots() # more than one plot in single figure
    # data
    bx = [0, 2, 4, 6, 8, 10, 12, 14]
    by = [0, 8 , 1, 3, 0, 10, 5, 4]
    cx = [0, 2, 4, 6, 8, 10, 12, 14]
    cy = [0, 2, 8, 10, 4, 2, 9, 4]
    # html graph styling
    fig.patch.set_facecolor('purple') # set outer bg
    ax.set_facecolor("#000") # set inner bg
    ax.set_xlabel('X-axis') # show x-label
    ax.set_ylabel('Y-axis') # show y-label
    ax.xaxis.label.set_color('hotpink') # set x-label color
    ax.yaxis.label.set_color('yellow') # set y-label color
    ax.plot(bx, by, linestyle = 'dotted', c = 'magenta')
    ax.plot(cx, cy, linestyle = 'dashed', c = 'white') 
    # save to temp buffer
    buf = BytesIO()
    fig.savefig(buf, format='png')
    # embed output in html
    data = base64.b64encode(buf.getbuffer()).decode('ascii')
    return f"<img src='data:image/png;base64,{data}'/>"
if __name__ == '__main__':
    app.run()