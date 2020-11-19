# Simple demo of reading each analog input from the ADS1x15 and printing it to
# the screen.
# Author: Tony DiCola
# License: Public Domain
import time

# Import the ADS1x15 module.
import Adafruit_ADS1x15


# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115(0x48)



# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1
#####
print('Reading ADS1x15 values, press Ctrl-C to quit...')
print('|     Canal {0:>6}     |       Canal {1:>6}   |'.format(*range(2)))
print('-' * 37)
##
values = [0]*2
valuess = [0]*2
for i in range(2):
    values[i] = adc.read_adc(i, gain=GAIN)
    valuess[i] = (values[i]*4.096)/32767
        
print('| {0:>6} V | {1:>6} V |'.format(*valuess))
time.sleep(0.5)
valuess
