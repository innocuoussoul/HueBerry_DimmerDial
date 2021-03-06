#!/usr/bin/env python

"""
how to create python menu
list all of the options, like 3 of them for now
button 1 goes up, button2 goes down
button 3 (gpio 23) is select
print 3 menu items, rectangle in the middle (auto gneerated)
shift the menu items up and down using relative positions. i.e. x + 10 x+ 20 x+ 30 and hten move x up and down by 10 
make sure the generated rectange is generated after the text (not that it matters)

"""

import time
import Adafruit_SSD1306
import RPi.GPIO as GPIO
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os

#selectheight = 

def display_menu(y_pos):
	# global y_pos
	# Clear image buffer by drawing a black filled box
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	
	#rectangle is xy and xy coordinates. draws a rectangle inbetween. 
	draw.rectangle((0,((disp.height/2)+6),width-1,((disp.height/2)-6)), outline=1, fill=0)

	# Set font type and size
	font = ImageFont.truetype('BMW.ttf', 12)
	#font = ImageFont.load_default()

	# Position bmw
	x_pos = (disp.width/2)-(string_width(font,"BMW")/2)    
	x_pos = x_pos + counter
	# Draw bmw
	draw.text((x_pos, y_pos), "BMW", font=font, fill=255)
	
	y_pos += 12
	x_pos = (disp.width/2)-(string_width(font,"The ultimate")/2)
	draw.text((x_pos,y_pos),"The ultimate", font=font, fill=255)
	
	y_pos += 12
	x_pos = (disp.width/2)-(string_width(font,"Driving machine")/2)
	draw.text((x_pos,y_pos),"Driving machine", font=font, fill=255)


	# Draw the image buffer
	disp.image(image)
	disp.display()

def display_time():
	# Collect current time and date
	if(time_format):
		current_time = time.strftime("%I:%M")
	else:
		current_time = time.strftime("%H:%M")
		
	current_date = time.strftime("%m / %d / %Y")

	# Clear image buffer by drawing a black filled box
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	# Set font type and size
	font = ImageFont.truetype('BMW.ttf', 40)
	#font = ImageFont.load_default()

	# Position time
	x_pos = (disp.width/2)-(string_width(font,current_time)/2)
	y_pos = 2 + (disp.height-4-8)/2 - (35/2)
        
	# Draw time
	draw.text((x_pos, y_pos), current_time, font=font, fill=255)

	# Set font type and size
	font = ImageFont.truetype('BMW.ttf', 13)
	#font = ImageFont.load_default()

	# Position date
	x_pos = (disp.width/2)-(string_width(font,current_date)/2)
	y_pos = disp.height-10

	# Draw date
	#draw.text((x_pos, y_pos), current_date, font=font, fill=255)

	# Draw the image buffer
	disp.image(image)
	disp.display()

def display_social():
	
	# Collect social media subscribers/followers/... by parsing webpages
	twitter = os.popen("curl https://twitter.com/fiveseven808?lang=en | grep 'data-nav=\"followers\"' | grep -o '[0-9]\+'").read()
	youtube = os.popen("curl https://www.youtube.com/c/FrederickVandenbosch | grep -o '[0-9|,]\+ subscribers' | grep -o '[0-9|,]\+'").read()
	facebook = "0"
	instagram = os.popen("curl https://www.instagram.com/f_vdbosch/ | grep -o '\"followed_by\":{\"count\":[0-9]\+}' | grep -o '[0-9]\+'").read()
	googleplus = "0"

	# Put data in lists that can be iterated over
	channels = ["YouTube", "Twitter", "Facebook", "Instagram", "Google+"]
	subscribers = [youtube, twitter, facebook, instagram, googleplus]

	# Clear image buffer by drawing a black filled box
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	# Set font type and size
	font = ImageFont.truetype('BMW.ttf', 11)
    #font = ImageFont.load_default()

	# Iterate over lists
	for i in range(0, 5):
		# Position channel name
		x_pos = 2
		y_pos = 2 + (((disp.height-4)/5)*i)

		# Draw channel name
		draw.text((x_pos, y_pos), channels[i], font=font, fill=255)

		# Position subcribers/followers/...
		x_pos = disp.width - 2 - string_width(font, subscribers[i])
		y_pos = 2 + (((disp.height-4)/5)*i)

		# Draw subcribers/followers/...
		draw.text((x_pos, y_pos), subscribers[i], font=font, fill=255)

	# Draw the image buffer
	disp.image(image)
	disp.display()

def display_network():
	# Collect network information by parsing command line outputs
	ipaddress = os.popen("ifconfig wlan0 | grep 'inet addr' | awk -F: '{print $2}' | awk '{print $1}'").read()
	netmask = os.popen("ifconfig wlan0 | grep 'Mask' | awk -F: '{print $4}'").read()
	gateway = os.popen("route -n | grep '^0.0.0.0' | awk '{print $2}'").read()
	ssid = os.popen("iwconfig wlan0 | grep 'ESSID' | awk '{print $4}' | awk -F\\\" '{print $2}'").read()

	# Clear image buffer by drawing a black filled box
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	# Set font type and size
	font = ImageFont.truetype('BMW.ttf', 16)
	#font = ImageFont.load_default()
        
	# Position SSID
	x_pos = 2
	y_pos = 2

	# Draw SSID
	draw.text((x_pos, y_pos), ssid, font=font, fill=255)
	
	# Set font type and size
	font = ImageFont.truetype('BMW.ttf', 11)
	#font = ImageFont.load_default()

	# Position IP
	y_pos += 12 + 10 
        
	# Draw IP
	draw.text((x_pos, y_pos), "IP: "+ipaddress, font=font, fill=255)

	# Position NM
	y_pos += 10 

	# Draw NM
	draw.text((x_pos, y_pos), "NM: "+netmask, font=font, fill=255)

	# Position GW
	y_pos += 10

	# Draw GW
	draw.text((x_pos, y_pos), "GW: "+gateway, font=font, fill=255)
	
	# Draw the image buffer
	disp.image(image)
	disp.display()
	
def display_ping():
	# Collect network information by parsing command line outputs
	pingtime = os.popen("ping -c 1 192.168.1.1 | grep time | awk -F=64 '{print $2}'").read()

	# Clear image buffer by drawing a black filled box
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	# Set font type and size
	font = ImageFont.truetype('BMW.ttf', 17)
	#font = ImageFont.load_default()
        
	# Position SSID
	x_pos = 2
	y_pos = 2

	# Draw SSID
	draw.text((x_pos, y_pos), "PingTime: ", font=font, fill=255)
	
	# Set font type and size
	font = ImageFont.truetype('BMW.ttf', 13)
	#font = ImageFont.load_default()

	# Position IP
	y_pos += 12 + 10 
        
	# Draw IP
	draw.text((x_pos, y_pos), pingtime, font=font, fill=255)
	
	# Draw the image buffer
	disp.image(image)
	disp.display()
	
def display_mika():
	# Clear image buffer by drawing a black filled box
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	# Set font type and size	
	font = ImageFont.truetype('BMW.ttf', 17)
	#font = ImageFont.load_default()
        
	# Position SSID
	x_pos = (disp.width/2)-(string_width(font,"I love you!")/2)
	y_pos = 2 + (disp.height-4-8)/2 - (35/2)

	# Draw SSID
	draw.text((x_pos, y_pos), "I love you!", font=font, fill=255)
	# Position date
	x_pos = (disp.width/2)-(string_width(font,"Mika!")/2)
	y_pos = disp.height-30

	# Draw date
	draw.text((x_pos, y_pos), "Mika!", font=font, fill=255)
	
	# Draw the image buffer
	disp.image(image)
	disp.display()

def display_custom(text):
	# Clear image buffer by drawing a black filled box
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	# Set font type and size
	#font = ImageFont.truetype('FreeMono.ttf', 8)
	font = ImageFont.load_default()
        
	# Position SSID
	x_pos = (width/2) - (string_width(font,text)/2)
	y_pos = (height/2) - (8/2)

	# Draw SSID
	draw.text((x_pos, y_pos), text, font=font, fill=255)

	# Draw the image buffer
	disp.image(image)
	disp.display()
	
def string_width(fontType,string):
	string_width = 0

	for i, c in enumerate(string):
		char_width, char_height = draw.textsize(c, font=fontType)
		string_width += char_width

	return string_width

# Set up GPIO with internal pull-up
GPIO.setmode(GPIO.BCM)	
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
# 128x64 display with hardware I2C
disp = Adafruit_SSD1306.SSD1306_128_64(rst=24)

# Initialize library
disp.begin()

# Get display width and height
width = disp.width
height = disp.height

# Clear display
disp.clear()
disp.display()

# Create image buffer with mode '1' for 1-bit color
image = Image.new('1', (width, height))

# Load default font
font = ImageFont.load_default()

# Create drawing object
draw = ImageDraw.Draw(image)

prev_millis = 0
prev_social = 0
display = 0
time_format = True

draw.rectangle((0,0,width,height), outline=0, fill=0)

# Set font type and size
font = ImageFont.truetype('BMW.ttf', 50)
#font = ImageFont.load_default()
# Position time
x_pos = (disp.width/2)-(string_width(font,"BMW")/2)
y_pos = 2 + (disp.height-4-8)/2 - (35/2)
    
# Draw time
draw.text((x_pos, y_pos), "BMW", font=font, fill=255)
#disp.dim(True)
#disp.set_contrast(0)
disp.image(image)
disp.display()
#time.sleep(1)

counter = 0
while True:
	millis = int(round(time.time() * 1000))
	y_pos = (disp.height/2) -4
	# Software debouncing
	if((millis - prev_millis) > 250):
		# Cycle through different displays
		if(not GPIO.input(20)):
			display += 1
			if(display > 4):
				display = 0
			prev_millis = int(round(time.time() * 1000))

		# Trigger action based on current display
		elif(not GPIO.input(7)):
			if(display == 0):
				# Toggle between 12/24h format
				time_format =  not time_format
				time.sleep(0.01)
			elif(display == 1):
				# Reconnect to network
				display_custom("reconnecting wifi ...")
				os.popen("sudo ifdown wlan0; sleep 5; sudo ifup --force wlan0")
				time.sleep(0.01)
			elif(display == 2):
				# Refresh social media now
				display_custom("fetching data ...")
				display_social()
				time.sleep(0.01)
			elif(display == 3):
				#display_custom("no data here...")
				display_ping()
				time.sleep(0.01)
			elif(display == 4):
				#display_custom("no data here...")
				display_mika()
				time.sleep(0.01)
			prev_millis = int(round(time.time() * 1000))

	if(display == 0):
		#display_time()
		display_menu(y_pos)
		prev_social = 0
	elif(display == 1):
		y_pos -= 12*1
		display_menu(y_pos)
		prev_social = 0
	elif(display == 2):
		y_pos -= 12*2
		display_menu(y_pos)
		prev_social = 0
	elif(display == 3):
		y_pos -= 12*3
		display_menu(y_pos)
		prev_social = 0
	elif(display == 4):
		display_mika()
		prev_social = 0

	time.sleep(0.1)
