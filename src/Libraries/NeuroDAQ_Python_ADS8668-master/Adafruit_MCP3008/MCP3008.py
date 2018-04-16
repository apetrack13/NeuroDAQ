import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import time

class MCP3008(object):
    """Class to represent an Adafruit MCP3008 analog to digital converter.
    """

    def __init__(self, clk=None, cs=None, miso=None, mosi=None, spi=None, gpio=None):
    
        self._spi = None

        if spi is not None:
            self._spi = spi
        elif clk is not None and cs is not None and miso is not None and mosi is not None:     
            if gpio is None:
                gpio = GPIO.get_platform_gpio()
            self._spi = SPI.BitBang(gpio, clk, mosi, miso, cs)
        else:
            raise ValueError('Must specify either spi for for hardware SPI or clk, cs, miso, and mosi for softwrare SPI!')
        self._spi.set_clock_hz(10000000)
        self._spi.set_mode(0)
        self._spi.set_bit_order(SPI.MSBFIRST)
        
        
    def read_all_ch(self, command):
    
        resp = self._spi.transfer([command, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])

        ch1_result = resp[2] << 4
        ch1_result |= resp[3] >> 4

        ch2_result = resp[4] << 4
        ch2_result |= resp[5] >> 4

        ch3_result = resp[6] << 4
        ch3_result |= resp[7] >> 4

        ch4_result = resp[8] << 4
        ch4_result |= resp[9] >> 4
        
        Results = (ch1_result, ch2_result, ch3_result, ch4_result)

        return Results
