"""
A simple Flask web application.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the IoT dashboard.
    """
    return render_template('index.html')

if __name__ == '__main__':
    # Running on 0.0.0.0 makes the app accessible from the network.
    # Debug mode is enabled for development.
    app.run(host='0.0.0.0', debug=True)
