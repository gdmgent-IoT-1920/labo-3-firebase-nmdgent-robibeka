from flask import Flask, request, render_template
from sense_hat import SenseHat

sense = SenseHat()
sense.set_imu_config(False, False, False)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/sensehat')
def sensehat():
    return render_template('sensehat.html')

host = '192.168.0.163'
port = 8080
if __name__ == '__main__':
    app.run(host=host, port=port, debug = True)
