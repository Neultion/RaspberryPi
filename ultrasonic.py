from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo = 21, trigger = 20)
while True:
    print(round(ultrasonic.distance*100,3))