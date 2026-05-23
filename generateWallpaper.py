from PIL import Image
from PIL import ImageDraw,ImageFont
from FetchContributions import graphdata,total,username
from datetime import datetime
import os
import ctypes

# THE TEXT 
im=Image.new(size=(1920,1080),mode='RGB')
squares=ImageDraw.Draw(im)
font2=ImageFont.truetype("AGENCYB.TTF",40)
squares.text((1675,1000),username,fill=(177, 186, 178),font=font2)
font1=ImageFont.truetype("AGENCYR.TTF",28)
font=ImageFont.truetype("AGENCYR.TTF",50)
squares.text((1650,80),"Total Contribution Data",fill=(255, 255, 255),font=font1)
squares.text((1700,140),str(total),fill=(255,255,255),font=font)


## Graph
square_size=30
gap=4
x_start = (1920 - (53 * (square_size + gap))) / 2
y_start = (1080 - (7 * (square_size + gap))) // 2
for i,week in enumerate(graphdata):
    weeklyContributions=week['contributionDays']
    for j,day in enumerate(weeklyContributions):
        x=x_start+i*(square_size+gap)
        y=y_start+j*(square_size+gap)
        if (day['contributionCount']==0):
            squares.rounded_rectangle(xy=(x,y,x+square_size,y+square_size),fill=(0, 0, 0),outline=(22, 33, 23),width=1,radius =4)
        
        elif (day['contributionCount']<=2):
            squares.rounded_rectangle(xy=(x,y,x+square_size,y+square_size),fill=(52, 140, 59),radius =4)
        elif (day['contributionCount']<=5):
            squares.rounded_rectangle(xy=(x,y,x+square_size,y+square_size),fill=(0, 109, 50),radius =4)
        elif (day['contributionCount']<=9):
            squares.rounded_rectangle(xy=(x,y,x+square_size,y+square_size),fill= (38, 166, 65),radius =4)
        else:
            squares.rounded_rectangle(xy=(x,y,x+square_size,y+square_size),fill= (57, 211, 83),radius =4)

## TIME STAMP

current_time=datetime.now()
date=current_time.strftime("%d/%m/%Y")
time=current_time.strftime("%H:%M")

squares.text((x_start,y_start-100),"Last Updated",fill=(255, 255, 255),font=font1)
squares.text((x_start,y_start-70),date,fill=(255, 255, 255),font=font1)
squares.text((x_start,y_start-40),time,fill=(255, 255, 255),font=font1)

## ADDING AS A WALLPAPER
im.save("wallpaper.png")
filename=os.path.abspath("wallpaper.png")
ctypes.windll.user32.SystemParametersInfoW(20,0,filename,3)
