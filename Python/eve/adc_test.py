import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from time import sleep

ads = ADS.ADS1015(i2c)

in0 = AnalogIn(ads, ADS.P0)
in1 = AnalogIn(ads, ADS.P1)
in2 = AnalogIn(ads, ADS.P2)
in3 = AnalogIn(ads, ADS.P3)

inArr = [in0, in1, in2, in3]

while True:
	for x,i in enumerate(inArr):
		print("Pin" , x , ": " , i.value, i.voltage)
	sleep(1)
