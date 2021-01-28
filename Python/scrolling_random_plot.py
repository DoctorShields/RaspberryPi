import Adafruit_SSD1306
from math import floor
from random import randint
from time import sleep
from PIL import Image, ImageDraw, ImageFont, ImageOps

RST=24
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
leftSide = 15
lineBot = 52
xDivs = 12
dx = floor((width-leftSide)/xDivs)

font = ImageFont.load_default()

# Create images; 1 = Bilevel, L = greyscale, RGB = true color
# The second image is just for my rotated text
img1 = Image.new('1', (width,height))
img2 = Image.new('1', (height,height))

# Create the drawing objects on the images
# Rotate img2 and paste it onto img1
draw1 = ImageDraw.Draw(img1)
draw2 = ImageDraw.Draw(img2)
draw2.text((20,2), "a(m/s2)", font=font, fill=255)
rot2 = img2.rotate(90)
img1.paste(rot2,(0,0,height,height))
draw1.line((leftSide, lineBot, width, lineBot),fill=255)
draw1.line((leftSide, lineBot, leftSide, 0), fill=255)
draw1.text((44,54), "time(s)", font=font, fill=255)
disp.image(img1)
disp.display()

# y data
yData = []
for i in range(xDivs+1):
	yData.append(22+randint(0,16))
print(yData)
i = 0
scrolling = False

def drawLine(i):
	x1 = leftSide + dx*i
	y1 = yData[i]
	x2 = leftSide + dx*(i+1)
	y2 = yData[i+1]
	draw1.line((x1,y1,x2,y2),fill=255)

while True:
	if not scrolling:
		drawLine(i)
		i += 1
		if i >= xDivs:
			scrolling = True
	else:
		# clear the screen
		draw1.rectangle((leftSide+1,0,width,lineBot-1),outline=0,fill=0)
		yData.append(22+randint(0,16))
		yData.pop(0)
		for i in range(xDivs):
			drawLine(i)
	disp.image(img1)
	disp.display()
	sleep(1)
