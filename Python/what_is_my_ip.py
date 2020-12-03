import time
import socket
import os
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

# Initialize library and clear display
disp.begin()
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Load default font.
font = ImageFont.load_default()

# Write two lines of text.
draw.text((0, 0),  'Finging IP Address...',  font=font, fill=255)

# Display image.
disp.image(image)
disp.display()

ipaddr = "---.---.---.---"
online = False

while not online:
	gw = os.popen("ip -4 route show default").read().split()
	if len(gw) > 0:
		print("Getting online...")
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect((gw[2],0))
		ipaddr = s.getsockname()[0]
		gateway = gw[2]
		host = socket.gethostname()
		online = True
	time.sleep(1)
	print("IP:", ipaddr, "GW:", gateway, "Host:", host)
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	draw.text((0,0), "My IP Address", font=font, fill=255)
	draw.text((0,20), ipaddr, font=font, fill=255)
	disp.image(image)
	disp.display()

