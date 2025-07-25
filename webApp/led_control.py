from flask import Flask, request, render_template
import RPi.GPIO as GPIO

LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

app = Flask(__name__)

@app.route('/led_control')
def led_control():
    return render_template('led_control.html')
@app.route('/led_control_act', methods = ['GET'])
def led_control_act():
    if request.method == 'GET':
        status = ''
        led = request.args['led']
        if led == '1':
            GPIO.output(LED, True)
            status = 'ON'
        else:
            GPIO.output(LED, False)
            status = 'OFF'
    return render_template('led_control.html', res = status)

if __name__ == '__main__':
    app.run(debug = True, port = 80, host = '0.0.0.0')