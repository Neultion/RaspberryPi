import time
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

def ReadVol(vol):
    adc = spi.xfer2([1, (8 + vol) << 4, 0])
    data = ((adc[1] & 3) << 8) +adc[2]
    return data

mcp3008 = 0
while True:
    a_1 = ReadVol(mcp3008)
    print('readVol : ', a_1, 'Voltage: ', 3.3*a_1/1024)
    time.sleep(0.5)

# from gpiozero import MCP3008
# from time import sleep
# pot = MCP3008(7)
# while True:
#     print(pot.value *100)
#     sleep(1)
