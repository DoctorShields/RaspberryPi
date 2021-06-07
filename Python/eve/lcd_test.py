import board
import busio
import time

from adafruit_is31fl3731.matrix import Matrix as Display

i2c = busio.I2C(board.SCL, board.SDA)

display = Display(i2c)

def displayPixels(xr):
#	print(xr)
	for x in range(0,16):
		for y in range(0,9):
			if x == xr:
				val = 100
			else:
				val = 0
			val = 255-abs(x-xr)*32
			if val < 0:
				val = 0
			display.pixel(x,y,val)
#			print(val)
'''
			if abs(x-xr) == 1:
				display.pixel(x,y,100)
			elif abs(x-xr) == 2:
				display.pixel(x,y,10)
			elif x == xr:
				display.pixel(x,y,255)
			else:
				display.pixel(x,y,0)
'''
row = 1
dr = 1

while True:
	displayPixels(row)
	row += dr
	if row == 16 or row == 0:
		dr *= -1
#	time.sleep(.02)
