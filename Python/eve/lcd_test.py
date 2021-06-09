import board
import busio
import time
from math import floor, sqrt

from adafruit_is31fl3731.matrix import Matrix as Display

i2c = busio.I2C(board.SCL, board.SDA)

display = Display(i2c)

rows = 9
cols = 16
drop = 50

def displayPixels(xr):
	for x in range(0,cols):
		for y in range(0,rows):
			dist = sqrt((x-xr)**2 + (floor(rows/2)-y)**2)
			val = 255-int(dist*drop)
#			val = 255-abs(x-xr)*drop-abs(floor(rows/2)-y)*drop
			if val < 0:
				val = 0
			display.pixel(x,y,val)
#			print(val)
row = 1
dr = 1

while True:
	displayPixels(row)
	row += dr
	if row == 16 or row == 0:
		dr *= -1
#	time.sleep(.02)
