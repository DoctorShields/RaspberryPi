import Adafruit_SSD1306

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

font = ImageFont.load_default()

img1 = Image.new('1', (128,64))
img2 = Image.new('1', (64,64))

draw1 = ImageDraw.Draw(img1)
draw2 = ImageDraw.Draw(img2)

# draw1.rectangle((0,0,128,64),outline=0, fill=255)
draw1.text((0,0), "time(s)", font=font, fill=255)
draw2.text((20,2), "a(m/s2)", font=font, fill=255)

rot2 = img2.rotate(90)
img1.paste(rot2,(0,0,64,64))
draw1.text((44,54), "time(s)", font=font, fill=255)
draw1.line((leftSide, lineBot, width, lineBot),fill=255)
draw1.line((leftSide, lineBot, leftSide, 0), fill=255)
disp.image(img1)
disp.display()
