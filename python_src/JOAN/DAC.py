import board
import busio
import time 
import adafruit_mcp4725
 
i2c = busio.I2C(board.SCL, board.SDA)
 
dac = adafruit_mcp4725.MCP4725(i2c, address=0x60)
print("¿Vout?")
Vout = int(input())
dac.value =Vout
time.sleep(1)

#dac.value =65535  
#time.sleep(0.9)
#dac.value =0  
#time.sleep(0.9)
#dac.value =32767 
#time.sleep(0.9)
#dac.value =0
#dac.value =21845 
#time.sleep(0.9)
#dac.value =0
