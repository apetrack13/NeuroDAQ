import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as gpio


def beginAcq(frequency, current, numChannels, impedance, duration, fileName):
    SPI_PORT = 0
    SPI_DEVICE = 0
    mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

    gpio.setmode(gpio.BCM)
    gpio.setup(26, gpio.OUT)
    gpio.output(26, gpio.LOW)
    gpio.output(26, gpio.HIGH)

    t1 = time.time() + duration
    # print(t1)
    with open(fileName, 'a+') as f:
        f.write('\n')

    print('Reading ADS8668 values, press Ctrl-C to quit...')

    # Main Loop
    while (time.time() < t1):
        values = []
        tempTime = [0]
        tempTime[0] = round(time.time() - t1 + duration, 4)

        if numChannels == 1:
           # Channel 1
            mcp.read_all_ch(0xC0)
            values0 = mcp.read_all_ch(0xC0)
            values0[0] = ((float(values0[0]) - 2046) / 197)   # ADC 1
            values0[1] = ((float(values0[1]) - 2046) / 197)   # ADC 2

            # Append samples to array
            values.extend(values0)
            values.extend(tempTime)

        elif (numChannels == 2):
            # Channel 1
            mcp.read_all_ch(0xC0)
            values0 = mcp.read_all_ch(0xC0)
            values0[0] = ((float(values0[0]) - 2046) / 197)  # ADC 1
            values0[1] = ((float(values0[1]) - 2046) / 197)  # ADC 2
            # Channel 2
            values0[2] = ((float(values0[2]) - 2046) / 197)  # ADC 3
            values0[3] = ((float(values0[3]) - 1535) / 195)  # ADC 4

            # Append samples to array
            values.extend(values0)
            values.extend(tempTime)

        elif numChannels == 3:
            # Channel 1
            mcp.read_all_ch(0xC0)
            values0 = mcp.read_all_ch(0xC0)
            values0[0] = ((float(values0[0]) - 2046) / 197)  # ADC 1
            values0[1] = ((float(values0[1]) - 2046) / 197)  # ADC 2
            # Channel 2
            values0[2] = ((float(values0[2]) - 2046) / 197)  # ADC 3
            values0[3] = ((float(values0[3]) - 1535) / 195)  # ADC 4
            # Channel 3
            mcp.read_all_ch(0xC4)
            values1 = mcp.read_all_ch(0xC4)
            values1[0] = ((float(values1[0]) - 2046) / 200)
            values1[1] = ((float(values1[1]) - 2046) / 200)
            # Append Samples to array
            values.extend(values0)
            values.extend(values1[0:2])
            values.extend(tempTime)

        elif numChannels == 4:
            # Channel 1
            mcp.read_all_ch(0xC0)
            values0 = mcp.read_all_ch(0xC0)
            values0[0] = ((float(values0[0]) - 2046) / 197)  # ADC 1
            values0[1] = ((float(values0[1]) - 2046) / 197)  # ADC 2
            # Channel 2
            values0[2] = ((float(values0[2]) - 2046) / 197)  # ADC 3
            values0[3] = ((float(values0[3]) - 1535) / 195)  # ADC 4
            # Channel 3
            mcp.read_all_ch(0xC4)
            values1 = mcp.read_all_ch(0xC4)
            values1[0] = ((float(values1[0]) - 2046) / 200)
            values1[1] = ((float(values1[1]) - 2046) / 200)
            # Channel 4
            values1[2] = ((float(values1[2]) - 1535) / 200)
            values1[3] = ((float(values1[3]) - 1535) / 200)
            # Append Samples to array
            values.extend(values0)
            values.extend(values1)
            values.extend(tempTime)

        elif numChannels == 5:
            # Channel 1
            mcp.read_all_ch(0xC0)
            values0 = mcp.read_all_ch(0xC0)
            values0[0] = ((float(values0[0]) - 2046) / 197)  # ADC 1
            values0[1] = ((float(values0[1]) - 2046) / 197)  # ADC 2
            # Channel 2
            values0[2] = ((float(values0[2]) - 2046) / 197)  # ADC 3
            values0[3] = ((float(values0[3]) - 1535) / 195)  # ADC 4
            # Channel 3
            mcp.read_all_ch(0xC4)
            values1 = mcp.read_all_ch(0xC4)
            values1[0] = ((float(values1[0]) - 2046) / 200)
            values1[1] = ((float(values1[1]) - 2046) / 200)
            # Channel 4
            values1[2] = ((float(values1[2]) - 1535) / 200)
            values1[3] = ((float(values1[3]) - 1535) / 200)
            # Channel 5
            mcp.read_all_ch(0xC8)
            values2 = mcp.read_all_ch(0xC4)
            values2[0] = ((float(values2[0]) - 2046) / 200)
            values2[1] = ((float(values2[1]) - 2046) / 200)
            # Append Samples to array
            values.extend(values0)
            values.extend(values1)
            values.extend(values2[0:2])
            values.extend(tempTime)

        elif numChannels == 6:
            mcp.read_all_ch(0xC0)
            values0 = mcp.read_all_ch(0xC0)
            # Channel 1
            values0[0] = ((float(values0[0]) - 2046) / 197)  # ADC 1
            values0[1] = ((float(values0[1]) - 2046) / 197)  # ADC 2
            # Channel 2
            values0[2] = ((float(values0[2]) - 2046) / 197)  # ADC 3
            values0[3] = ((float(values0[3]) - 1535) / 195)  # ADC 4
            mcp.read_all_ch(0xC4)
            values1 = mcp.read_all_ch(0xC4)
            # Channel 3
            values1[0] = ((float(values1[0]) - 2046) / 200)
            values1[1] = ((float(values1[1]) - 2046) / 200)
            # Channel 4
            values1[2] = ((float(values1[2]) - 1535) / 200)
            values1[3] = ((float(values1[3]) - 1535) / 200)
            mcp.read_all_ch(0xC8)
            values2 = mcp.read_all_ch(0xC4)
            # Channel 5
            values2[0] = ((float(values2[0]) - 2046) / 200)
            values2[1] = ((float(values2[1]) - 2046) / 200)
            # Channel 6
            values2[2] = ((float(values2[2]) - 1535) / 200)
            values2[3] = ((float(values2[3]) - 1535) / 200)
            # Append Samples to array
            values.extend(values0)
            values.extend(values1)
            values.extend(values2)
            values.extend(tempTime)

        elif numChannels == 7:
            mcp.read_all_ch(0xC0)
            values0 = mcp.read_all_ch(0xC0)
            # Channel 1
            values0[0] = ((float(values0[0]) - 2046) / 197)  # ADC 1
            values0[1] = ((float(values0[1]) - 2046) / 197)  # ADC 2
            # Channel 2
            values0[2] = ((float(values0[2]) - 2046) / 197)  # ADC 3
            values0[3] = ((float(values0[3]) - 1535) / 195)  # ADC 4
            mcp.read_all_ch(0xC4)
            values1 = mcp.read_all_ch(0xC4)
            # Channel 3
            values1[0] = ((float(values1[0]) - 2046) / 200)
            values1[1] = ((float(values1[1]) - 2046) / 200)
            # Channel 4
            values1[2] = ((float(values1[2]) - 1535) / 200)
            values1[3] = ((float(values1[3]) - 1535) / 200)
            mcp.read_all_ch(0xC8)
            values2 = mcp.read_all_ch(0xC4)
            # Channel 5
            values2[0] = ((float(values2[0]) - 2046) / 200)
            values2[1] = ((float(values2[1]) - 2046) / 200)
            # Channel 6
            values2[2] = ((float(values2[2]) - 1535) / 200)
            values2[3] = ((float(values2[3]) - 1535) / 200)
            mcp.read_all_ch(0xCC)
            values3 = mcp.read_all_ch(0xCC)
            # Channel 7
            values3[0] = ((float(values3[0]) - 1520) / 205)
            values3[1] = ((float(values3[1]) - 1520) / 205)
            # Append Samples to array
            values.extend(values0)
            values.extend(values1)
            values.extend(values2)
            values.extend(values3[0:2])
            values.extend(tempTime)
        elif numChannels == 8:
            mcp.read_all_ch(0xC0)
            values0 = mcp.read_all_ch(0xC0)
            # Channel 1
            values0[0] = ((float(values0[0]) - 2046) / 197)  # ADC 1
            values0[1] = ((float(values0[1]) - 2046) / 197)  # ADC 2
            # Channel 2
            values0[2] = ((float(values0[2]) - 2046) / 197)  # ADC 3
            values0[3] = ((float(values0[3]) - 1535) / 195)  # ADC 4
            mcp.read_all_ch(0xC4)
            values1 = mcp.read_all_ch(0xC4)
            # Channel 3
            values1[0] = ((float(values1[0]) - 2046) / 200)
            values1[1] = ((float(values1[1]) - 2046) / 200)
            # Channel 4
            values1[2] = ((float(values1[2]) - 1535) / 200)
            values1[3] = ((float(values1[3]) - 1535) / 200)
            mcp.read_all_ch(0xC8)
            values2 = mcp.read_all_ch(0xC4)
            # Channel 5
            values2[0] = ((float(values2[0]) - 2046) / 200)
            values2[1] = ((float(values2[1]) - 2046) / 200)
            # Channel 6
            values2[2] = ((float(values2[2]) - 1535) / 200)
            values2[3] = ((float(values2[3]) - 1535) / 200)
            mcp.read_all_ch(0xCC)
            values3 = mcp.read_all_ch(0xCC)
            # Channel 7
            values3[0] = ((float(values3[0]) - 1520) / 205)
            values3[1] = ((float(values3[1]) - 1520) / 205)
            # Channel 8
            values3[2] = ((float(values3[2]) - 2045) / 205)
            values3[3] = ((float(values3[3]) - 2045) / 205)
            # Append Samples to array
            values.extend(values0)
            values.extend(values1)
            values.extend(values2)
            values.extend(values3)
            values.extend(tempTime)

        elif numChannels == 9:
            mcp.read_all_ch(0xC0)
            values0 = mcp.read_all_ch(0xC0)
            # Channel 1
            values0[0] = ((float(values0[0]) - 2046) / 197)  # ADC 1
            values0[1] = ((float(values0[1]) - 2046) / 197)  # ADC 2
            # Channel 2
            values0[2] = ((float(values0[2]) - 2046) / 197)  # ADC 3
            values0[3] = ((float(values0[3]) - 1535) / 195)  # ADC 4
            mcp.read_all_ch(0xC4)
            values1 = mcp.read_all_ch(0xC4)
            # Channel 3
            values1[0] = ((float(values1[0]) - 2046) / 200)
            values1[1] = ((float(values1[1]) - 2046) / 200)
            # Channel 4
            values1[2] = ((float(values1[2]) - 1535) / 200)
            values1[3] = ((float(values1[3]) - 1535) / 200)
            mcp.read_all_ch(0xC8)
            values2 = mcp.read_all_ch(0xC4)
            # Channel 5
            values2[0] = ((float(values2[0]) - 2046) / 200)
            values2[1] = ((float(values2[1]) - 2046) / 200)
            # Channel 6
            values2[2] = ((float(values2[2]) - 1535) / 200)
            values2[3] = ((float(values2[3]) - 1535) / 200)
            mcp.read_all_ch(0xCC)
            values3 = mcp.read_all_ch(0xCC)
            # Channel 7
            values3[0] = ((float(values3[0]) - 1520) / 205)
            values3[1] = ((float(values3[1]) - 1520) / 205)
            # Channel 8
            values3[2] = ((float(values3[2]) - 2045) / 205)
            values3[3] = ((float(values3[3]) - 2045) / 205)
            mcp.read_all_ch(0xD0)
            values4 = mcp.read_all_ch(0xD0)
            # Channel 9
            values4[0] = ((float(values4[0]) - 2045) / 205)
            values4[1] = ((float(values4[1]) - 2045) / 205)
            # Append Samples to array
            values.extend(values0)
            values.extend(values1)
            values.extend(values2)
            values.extend(values3)
            values.extend(values4[0:2])
            values.extend(tempTime)

        elif numChannels == 10:
            mcp.read_all_ch(0xC0)
            values0 = mcp.read_all_ch(0xC0)
            # Channel 1
            values0[0] = ((float(values0[0]) - 2046) / 197)  # ADC 1
            values0[1] = ((float(values0[1]) - 2046) / 197)  # ADC 2
            # Channel 2
            values0[2] = ((float(values0[2]) - 2046) / 197)  # ADC 3
            values0[3] = ((float(values0[3]) - 1535) / 195)  # ADC 4
            mcp.read_all_ch(0xC4)
            values1 = mcp.read_all_ch(0xC4)
            # Channel 3
            values1[0] = ((float(values1[0]) - 2046) / 200)
            values1[1] = ((float(values1[1]) - 2046) / 200)
            # Channel 4
            values1[2] = ((float(values1[2]) - 1535) / 200)
            values1[3] = ((float(values1[3]) - 1535) / 200)
            mcp.read_all_ch(0xC8)
            values2 = mcp.read_all_ch(0xC4)
            # Channel 5
            values2[0] = ((float(values2[0]) - 2046) / 200)
            values2[1] = ((float(values2[1]) - 2046) / 200)
            # Channel 6
            values2[2] = ((float(values2[2]) - 1535) / 200)
            values2[3] = ((float(values2[3]) - 1535) / 200)
            mcp.read_all_ch(0xCC)
            values3 = mcp.read_all_ch(0xCC)
            # Channel 7
            values3[0] = ((float(values3[0]) - 1520) / 205)
            values3[1] = ((float(values3[1]) - 1520) / 205)
            # Channel 8
            values3[2] = ((float(values3[2]) - 2045) / 205)
            values3[3] = ((float(values3[3]) - 2045) / 205)
            mcp.read_all_ch(0xD0)
            values4 = mcp.read_all_ch(0xD0)
            # Channel 9
            values4[0] = ((float(values4[0]) - 2045) / 205)
            values4[1] = ((float(values4[1]) - 2045) / 205)
            # Channel 10
            values4[2] = ((float(values4[2]) - 2045) / 205)
            values4[3] = ((float(values4[3]) - 2045) / 205)
            # Append Samples to array
            values.extend(values0)
            values.extend(values1)
            values.extend(values2)
            values.extend(values3)
            values.extend(values4)
            values.extend(tempTime)
        elif numChannels == 11:
            mcp.read_all_ch(0xC0)
            values0 = mcp.read_all_ch(0xC0)
            # Channel 1
            values0[0] = ((float(values0[0]) - 2046) / 197)  # ADC 1
            values0[1] = ((float(values0[1]) - 2046) / 197)  # ADC 2
            # Channel 2
            values0[2] = ((float(values0[2]) - 2046) / 197)  # ADC 3
            values0[3] = ((float(values0[3]) - 1535) / 195)  # ADC 4
            mcp.read_all_ch(0xC4)
            values1 = mcp.read_all_ch(0xC4)
            # Channel 3
            values1[0] = ((float(values1[0]) - 2046) / 200)
            values1[1] = ((float(values1[1]) - 2046) / 200)
            # Channel 4
            values1[2] = ((float(values1[2]) - 1535) / 200)
            values1[3] = ((float(values1[3]) - 1535) / 200)
            mcp.read_all_ch(0xC8)
            values2 = mcp.read_all_ch(0xC4)
            # Channel 5
            values2[0] = ((float(values2[0]) - 2046) / 200)
            values2[1] = ((float(values2[1]) - 2046) / 200)
            # Channel 6
            values2[2] = ((float(values2[2]) - 1535) / 200)
            values2[3] = ((float(values2[3]) - 1535) / 200)
            mcp.read_all_ch(0xCC)
            values3 = mcp.read_all_ch(0xCC)
            # Channel 7
            values3[0] = ((float(values3[0]) - 1520) / 205)
            values3[1] = ((float(values3[1]) - 1520) / 205)
            # Channel 8
            values3[2] = ((float(values3[2]) - 2045) / 205)
            values3[3] = ((float(values3[3]) - 2045) / 205)
            mcp.read_all_ch(0xD0)
            values4 = mcp.read_all_ch(0xD0)
            # Channel 9
            values4[0] = ((float(values4[0]) - 2045) / 205)
            values4[1] = ((float(values4[1]) - 2045) / 205)
            # Channel 10
            values4[2] = ((float(values4[2]) - 2045) / 205)
            values4[3] = ((float(values4[3]) - 2045) / 205)
            mcp.read_all_ch(0xD4)
            values5 = mcp.read_all_ch(0xD4)
            # Channel 11
            values5[0] = ((float(values5[0]) - 2045) / 205)
            values5[1] = ((float(values5[1]) - 2045) / 205)
            # Append Samples to array
            values.extend(values0)
            values.extend(values1)
            values.extend(values2)
            values.extend(values3)
            values.extend(values4)
            values.extend(values5[0:2])
            values.extend(tempTime)

        elif numChannels == 12:
            mcp.read_all_ch(0xC0)
            values0 = mcp.read_all_ch(0xC0)
            # Channel 1
            values0[0] = ((float(values0[0]) - 2046) / 197)  # ADC 1
            values0[1] = ((float(values0[1]) - 2046) / 197)  # ADC 2
            # Channel 2
            values0[2] = ((float(values0[2]) - 2046) / 197)  # ADC 3
            values0[3] = ((float(values0[3]) - 1535) / 195)  # ADC 4
            mcp.read_all_ch(0xC4)
            values1 = mcp.read_all_ch(0xC4)
            # Channel 3
            values1[0] = ((float(values1[0]) - 2046) / 200)
            values1[1] = ((float(values1[1]) - 2046) / 200)
            # Channel 4
            values1[2] = ((float(values1[2]) - 1535) / 200)
            values1[3] = ((float(values1[3]) - 1535) / 200)
            mcp.read_all_ch(0xC8)
            values2 = mcp.read_all_ch(0xC4)
            # Channel 5
            values2[0] = ((float(values2[0]) - 2046) / 200)
            values2[1] = ((float(values2[1]) - 2046) / 200)
            # Channel 6
            values2[2] = ((float(values2[2]) - 1535) / 200)
            values2[3] = ((float(values2[3]) - 1535) / 200)
            mcp.read_all_ch(0xCC)
            values3 = mcp.read_all_ch(0xCC)
            # Channel 7
            values3[0] = ((float(values3[0]) - 1520) / 205)
            values3[1] = ((float(values3[1]) - 1520) / 205)
            # Channel 8
            values3[2] = ((float(values3[2]) - 2045) / 205)
            values3[3] = ((float(values3[3]) - 2045) / 205)
            mcp.read_all_ch(0xD0)
            values4 = mcp.read_all_ch(0xD0)
            # Channel 9
            values4[0] = ((float(values4[0]) - 2045) / 205)
            values4[1] = ((float(values4[1]) - 2045) / 205)
            # Channel 10
            values4[2] = ((float(values4[2]) - 2045) / 205)
            values4[3] = ((float(values4[3]) - 2045) / 205)
            mcp.read_all_ch(0xD4)
            values5 = mcp.read_all_ch(0xD4)
            # Channel 11
            values5[0] = ((float(values5[0]) - 2045) / 205)
            values5[1] = ((float(values5[1]) - 2045) / 205)
            # Channel 12
            values5[2] = ((float(values5[2]) - 2045) / 205)
            values5[3] = ((float(values5[3]) - 2045) / 205)
            # Append Samples to array
            values.extend(values0)
            values.extend(values1)
            values.extend(values2)
            values.extend(values3)
            values.extend(values4)
            values.extend(values5)
            values.extend(tempTime)

        elif numChannels ==13:
            mcp.read_all_ch(0xC0)
            values0 = mcp.read_all_ch(0xC0)
            # Channel 1
            values0[0] = ((float(values0[0]) - 2046) / 197)  # ADC 1
            values0[1] = ((float(values0[1]) - 2046) / 197)  # ADC 2
            # Channel 2
            values0[2] = ((float(values0[2]) - 2046) / 197)  # ADC 3
            values0[3] = ((float(values0[3]) - 1535) / 195)  # ADC 4
            mcp.read_all_ch(0xC4)
            values1 = mcp.read_all_ch(0xC4)
            # Channel 3
            values1[0] = ((float(values1[0]) - 2046) / 200)
            values1[1] = ((float(values1[1]) - 2046) / 200)
            # Channel 4
            values1[2] = ((float(values1[2]) - 1535) / 200)
            values1[3] = ((float(values1[3]) - 1535) / 200)
            mcp.read_all_ch(0xC8)
            values2 = mcp.read_all_ch(0xC4)
            # Channel 5
            values2[0] = ((float(values2[0]) - 2046) / 200)
            values2[1] = ((float(values2[1]) - 2046) / 200)
            # Channel 6
            values2[2] = ((float(values2[2]) - 1535) / 200)
            values2[3] = ((float(values2[3]) - 1535) / 200)
            mcp.read_all_ch(0xCC)
            values3 = mcp.read_all_ch(0xCC)
            # Channel 7
            values3[0] = ((float(values3[0]) - 1520) / 205)
            values3[1] = ((float(values3[1]) - 1520) / 205)
            # Channel 8
            values3[2] = ((float(values3[2]) - 2045) / 205)
            values3[3] = ((float(values3[3]) - 2045) / 205)
            mcp.read_all_ch(0xD0)
            values4 = mcp.read_all_ch(0xD0)
            # Channel 9
            values4[0] = ((float(values4[0]) - 2045) / 205)
            values4[1] = ((float(values4[1]) - 2045) / 205)
            # Channel 10
            values4[2] = ((float(values4[2]) - 2045) / 205)
            values4[3] = ((float(values4[3]) - 2045) / 205)
            mcp.read_all_ch(0xD4)
            values5 = mcp.read_all_ch(0xD4)
            # Channel 11
            values5[0] = ((float(values5[0]) - 2045) / 205)
            values5[1] = ((float(values5[1]) - 2045) / 205)
            # Channel 12
            values5[2] = ((float(values5[2]) - 2045) / 205)
            values5[3] = ((float(values5[3]) - 2045) / 205)
            mcp.read_all_ch(0xD8)
            values6 = mcp.read_all_ch(0xD8)
            # Channel 13
            values6[0] = ((float(values6[0]) - 2045) / 205)
            values6[1] = ((float(values6[1]) - 2045) / 205)

            # Append Samples to array
            values.extend(values0)
            values.extend(values1)
            values.extend(values2)
            values.extend(values3)
            values.extend(values4)
            values.extend(values5)
            values.extend(values6[0:2])
            values.extend(tempTime)

        elif numChannels == 14:
            mcp.read_all_ch(0xC0)
            values0 = mcp.read_all_ch(0xC0)
            # Channel 1
            values0[0] = ((float(values0[0]) - 2046) / 197)  # ADC 1
            values0[1] = ((float(values0[1]) - 2046) / 197)  # ADC 2
            # Channel 2
            values0[2] = ((float(values0[2]) - 2046) / 197)  # ADC 3
            values0[3] = ((float(values0[3]) - 1535) / 195)  # ADC 4
            mcp.read_all_ch(0xC4)
            values1 = mcp.read_all_ch(0xC4)
            # Channel 3
            values1[0] = ((float(values1[0]) - 2046) / 200)
            values1[1] = ((float(values1[1]) - 2046) / 200)
            # Channel 4
            values1[2] = ((float(values1[2]) - 1535) / 200)
            values1[3] = ((float(values1[3]) - 1535) / 200)
            mcp.read_all_ch(0xC8)
            values2 = mcp.read_all_ch(0xC4)
            # Channel 5
            values2[0] = ((float(values2[0]) - 2046) / 200)
            values2[1] = ((float(values2[1]) - 2046) / 200)
            # Channel 6
            values2[2] = ((float(values2[2]) - 1535) / 200)
            values2[3] = ((float(values2[3]) - 1535) / 200)
            mcp.read_all_ch(0xCC)
            values3 = mcp.read_all_ch(0xCC)
            # Channel 7
            values3[0] = ((float(values3[0]) - 1520) / 205)
            values3[1] = ((float(values3[1]) - 1520) / 205)
            # Channel 8
            values3[2] = ((float(values3[2]) - 2045) / 205)
            values3[3] = ((float(values3[3]) - 2045) / 205)
            mcp.read_all_ch(0xD0)
            values4 = mcp.read_all_ch(0xD0)
            # Channel 9
            values4[0] = ((float(values4[0]) - 2045) / 205)
            values4[1] = ((float(values4[1]) - 2045) / 205)
            # Channel 10
            values4[2] = ((float(values4[2]) - 2045) / 205)
            values4[3] = ((float(values4[3]) - 2045) / 205)
            mcp.read_all_ch(0xD4)
            values5 = mcp.read_all_ch(0xD4)
            # Channel 11
            values5[0] = ((float(values5[0]) - 2045) / 205)
            values5[1] = ((float(values5[1]) - 2045) / 205)
            # Channel 12
            values5[2] = ((float(values5[2]) - 2045) / 205)
            values5[3] = ((float(values5[3]) - 2045) / 205)
            mcp.read_all_ch(0xD8)
            values6 = mcp.read_all_ch(0xD8)
            # Channel 13
            values6[0] = ((float(values6[0]) - 2045) / 205)
            values6[1] = ((float(values6[1]) - 2045) / 205)
            # Channel 14
            values6[2] = ((float(values6[2]) - 2045) / 205)
            values6[3] = ((float(values6[3]) - 2045) / 205)

            # Append Samples to array
            values.extend(values0)
            values.extend(values1)
            values.extend(values2)
            values.extend(values3)
            values.extend(values4)
            values.extend(values5)
            values.extend(values6)
            values.extend(tempTime)

        elif numChannels == 15:
            mcp.read_all_ch(0xC0)
            values0 = mcp.read_all_ch(0xC0)
            # Channel 1
            values0[0] = ((float(values0[0]) - 2046) / 197)  # ADC 1
            values0[1] = ((float(values0[1]) - 2046) / 197)  # ADC 2
            # Channel 2
            values0[2] = ((float(values0[2]) - 2046) / 197)  # ADC 3
            values0[3] = ((float(values0[3]) - 1535) / 195)  # ADC 4
            mcp.read_all_ch(0xC4)
            values1 = mcp.read_all_ch(0xC4)
            # Channel 3
            values1[0] = ((float(values1[0]) - 2046) / 200)
            values1[1] = ((float(values1[1]) - 2046) / 200)
            # Channel 4
            values1[2] = ((float(values1[2]) - 1535) / 200)
            values1[3] = ((float(values1[3]) - 1535) / 200)
            mcp.read_all_ch(0xC8)
            values2 = mcp.read_all_ch(0xC4)
            # Channel 5
            values2[0] = ((float(values2[0]) - 2046) / 200)
            values2[1] = ((float(values2[1]) - 2046) / 200)
            # Channel 6
            values2[2] = ((float(values2[2]) - 1535) / 200)
            values2[3] = ((float(values2[3]) - 1535) / 200)
            mcp.read_all_ch(0xCC)
            values3 = mcp.read_all_ch(0xCC)
            # Channel 7
            values3[0] = ((float(values3[0]) - 1520) / 205)
            values3[1] = ((float(values3[1]) - 1520) / 205)
            # Channel 8
            values3[2] = ((float(values3[2]) - 2045) / 205)
            values3[3] = ((float(values3[3]) - 2045) / 205)
            mcp.read_all_ch(0xD0)
            values4 = mcp.read_all_ch(0xD0)
            # Channel 9
            values4[0] = ((float(values4[0]) - 2045) / 205)
            values4[1] = ((float(values4[1]) - 2045) / 205)
            # Channel 10
            values4[2] = ((float(values4[2]) - 2045) / 205)
            values4[3] = ((float(values4[3]) - 2045) / 205)
            mcp.read_all_ch(0xD4)
            values5 = mcp.read_all_ch(0xD4)
            # Channel 11
            values5[0] = ((float(values5[0]) - 2045) / 205)
            values5[1] = ((float(values5[1]) - 2045) / 205)
            # Channel 12
            values5[2] = ((float(values5[2]) - 2045) / 205)
            values5[3] = ((float(values5[3]) - 2045) / 205)
            mcp.read_all_ch(0xD8)
            values6 = mcp.read_all_ch(0xD8)
            # Channel 13
            values6[0] = ((float(values6[0]) - 2045) / 205)
            values6[1] = ((float(values6[1]) - 2045) / 205)
            # Channel 14
            values6[2] = ((float(values6[2]) - 2045) / 205)
            values6[3] = ((float(values6[3]) - 2045) / 205)
            mcp.read_all_ch(0xDC)
            values7 = mcp.read_all_ch(0xDC)
            # Channel 15
            values7[0] = ((float(values7[0]) - 2045) / 205)
            values7[1] = ((float(values7[1]) - 2045) / 205)

            # Append Samples to array
            values.extend(values0)
            values.extend(values1)
            values.extend(values2)
            values.extend(values3)
            values.extend(values4)
            values.extend(values5)
            values.extend(values6)
            values.extend(values7[0:2])
            values.extend(tempTime)

        elif numChannels == 16:
            mcp.read_all_ch(0xC0)
            values0 = mcp.read_all_ch(0xC0)
            # Channel 1
            values0[0] = ((float(values0[0]) - 2046) / 197)  # ADC 1
            values0[1] = ((float(values0[1]) - 2046) / 197)  # ADC 2
            # Channel 2
            values0[2] = ((float(values0[2]) - 2046) / 197)  # ADC 3
            values0[3] = ((float(values0[3]) - 1535) / 195)  # ADC 4
            mcp.read_all_ch(0xC4)
            values1 = mcp.read_all_ch(0xC4)
            # Channel 3
            values1[0] = ((float(values1[0]) - 2046) / 200)
            values1[1] = ((float(values1[1]) - 2046) / 200)
            # Channel 4
            values1[2] = ((float(values1[2]) - 1535) / 200)
            values1[3] = ((float(values1[3]) - 1535) / 200)
            mcp.read_all_ch(0xC8)
            values2 = mcp.read_all_ch(0xC4)
            # Channel 5
            values2[0] = ((float(values2[0]) - 2046) / 200)
            values2[1] = ((float(values2[1]) - 2046) / 200)
            # Channel 6
            values2[2] = ((float(values2[2]) - 1535) / 200)
            values2[3] = ((float(values2[3]) - 1535) / 200)
            mcp.read_all_ch(0xCC)
            values3 = mcp.read_all_ch(0xCC)
            # Channel 7
            values3[0] = ((float(values3[0]) - 1520) / 205)
            values3[1] = ((float(values3[1]) - 1520) / 205)
            # Channel 8
            values3[2] = ((float(values3[2]) - 2045) / 205)
            values3[3] = ((float(values3[3]) - 2045) / 205)
            mcp.read_all_ch(0xD0)
            values4 = mcp.read_all_ch(0xD0)
            # Channel 9
            values4[0] = ((float(values4[0]) - 2045) / 205)
            values4[1] = ((float(values4[1]) - 2045) / 205)
            # Channel 10
            values4[2] = ((float(values4[2]) - 2045) / 205)
            values4[3] = ((float(values4[3]) - 2045) / 205)
            mcp.read_all_ch(0xD4)
            values5 = mcp.read_all_ch(0xD4)
            # Channel 11
            values5[0] = ((float(values5[0]) - 2045) / 205)
            values5[1] = ((float(values5[1]) - 2045) / 205)
            # Channel 12
            values5[2] = ((float(values5[2]) - 2045) / 205)
            values5[3] = ((float(values5[3]) - 2045) / 205)
            mcp.read_all_ch(0xD8)
            values6 = mcp.read_all_ch(0xD8)
            # Channel 13
            values6[0] = ((float(values6[0]) - 2045) / 205)
            values6[1] = ((float(values6[1]) - 2045) / 205)
            # Channel 14
            values6[2] = ((float(values6[2]) - 2045) / 205)
            values6[3] = ((float(values6[3]) - 2045) / 205)
            mcp.read_all_ch(0xDC)
            values7 = mcp.read_all_ch(0xDC)
            # Channel 15
            values7[0] = ((float(values7[0]) - 2045) / 205)
            values7[1] = ((float(values7[1]) - 2045) / 205)
            # Channel 16
            values7[2] = ((float(values7[2]) - 2045) / 205)
            values7[3] = ((float(values7[3]) - 1520) / 205)

            # Append Samples to array
            values.extend(values0)
            values.extend(values1)
            values.extend(values2)
            values.extend(values3)
            values.extend(values4)
            values.extend(values5)
            values.extend(values6)
            values.extend(values7)
            values.extend(tempTime)

        with open(fileName, 'a+') as f:
            f.write((", ".join(str(x) for x in values)))
            f.write('\n')
    print('Test Complete')
    print(fileName)
