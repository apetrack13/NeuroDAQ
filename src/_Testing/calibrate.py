import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as gpio

#command = int(sys.argv[1], 16)
resistance = 10000
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

gpio.setmode(gpio.BCM)
gpio.setup(26, gpio.OUT)
gpio.output(26, gpio.LOW)
gpio.output(26, gpio.HIGH)


while True:
    values1 = mcp.read_all_ch(0xC0)
    values1[0] = ((float(values1[0]) - 2046) / 200)
    values1[1] = ((float(values1[1]) - 2046) / 200)
    values1[2] = ((float(values1[2]) - 1535) / 200)
    values1[3] = ((float(values1[3]) - 1535) / 200)
    print(values1)
    time.sleep(1)
