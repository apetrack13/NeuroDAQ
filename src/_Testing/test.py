import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as gpio
import sys

#command = int(sys.argv[1], 16)

SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

gpio.setmode(gpio.BCM)
gpio.setup(26, gpio.OUT)
gpio.output(26, gpio.LOW)
gpio.output(26, gpio.HIGH)

##appendFile = open('data.csv','w+')
##appendFile.write('\n')
##appendFile.close()

print('Reading ADS8668 values, press Ctrl-C to quit...')

#mcp.setRegisters(0x0)

# Main Loop
while True:
    value = mcp.read_all_ch(0xC0)
    print(value)
    time.sleep(0.5)
    
    
