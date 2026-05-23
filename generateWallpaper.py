from PIL import Image
from PIL import ImageDraw
from FetchContributions import graphdata
import os
import ctypes
im=Image.new(size=(1920,1080),mode='RGB')
squares=ImageDraw.Draw(im)

for i,week in enumerate(graphdata):
    weeklyContributions=week['contributionDays']
    for j,day in enumerate(weeklyContributions):
        x=300+i*(20+3)
        y=400+j*(20+3)
        if (day['contributionCount']==0):
            squares.rounded_rectangle(xy=(x,y,x+20,y+20),fill=(0, 0, 0),outline=(22, 33, 23),width=1,radius =4)
        
        elif (day['contributionCount']<=2):
            squares.rounded_rectangle(xy=(x,y,x+20,y+20),fill=(52, 140, 59),radius =4)
        elif (day['contributionCount']<=5):
            squares.rounded_rectangle(xy=(x,y,x+20,y+20),fill=(0, 109, 50),radius =4)
        elif (day['contributionCount']<=9):
            squares.rounded_rectangle(xy=(x,y,x+20,y+20),fill= (38, 166, 65),radius =4)
        else:
            squares.rounded_rectangle(xy=(x,y,x+20,y+20),fill= (57, 211, 83),radius =4)
im.save("wallpaper.png")
filename=os.path.abspath("wallpaper.png")
ctypes.windll.user32.SystemParametersInfoW(20,0,filename,3)