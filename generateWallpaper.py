from PIL import Image
from PIL import ImageDraw
from FetchContributions import graphdata


im=Image.new(size=(1010,1010),mode='RGB')
squares=ImageDraw.Draw(im)

for week in graphdata:
    weeklyContributions=week['contributionDays']
    for day in weeklyContributions:
        print(f"Today's date: {day['date']}\n Contributions Made Today: {day['contributionCount']}")
        for i in range(53):
    for j in range(7):
        x=5+i*(20+20)
        y=5+j*(20+20)
        squares.rectangle(xy=(x,y,x+20,y+20),fill=(52, 140, 59))

im.show()