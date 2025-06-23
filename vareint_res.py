import spidev
import time

def analog_read(channel):
    r = spi.xfer2([1, (8+channel)<<4, 0])
    adc_out = ((r[1]&0x03)<<8) | r[2]
    return adc_out

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

try:
    while True:
        adc = analog_read(2)
        voltage = adc*3.3/1023
        print("ADC = %d Voltage = %.3fV" % (adc, voltage))
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    spi.close()