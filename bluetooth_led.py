import RPi.GPIO as GPIO
import serial

LED = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

ser = serial.Serial('/dev/rfcomm0', 115200)
ser.close()
ser.open()

str = b'Bluetooth LED Control\r\n'
n = ser.write(str)
try:
    while True:
        if ser.readable():
            response = ser.readline()
            if response == b'ON\n':
                GPIO.output(LED, True)
            elif response == b'OFF\n':
                GPIO.output(LED, False)
            print(response)
except KeyboardInterrupt:
    pass
finally:
    ser.close()
