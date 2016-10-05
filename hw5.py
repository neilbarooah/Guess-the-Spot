# Neil Barooah
# Section - A2
# neilbarooah@gatech.edu
# My partner, Raghav Maheshwari , and I worked on this assignment alone, using only this semester's resources.

from Graphics import *
from Myro import *
import math
import random


win = Window("Guess the Spot!", 800,800)
win.setBackground(Color("lightblue"))

score = 0
z = 1

try:
    fin = open("spot.txt", "r")
    highscore = fin.readline()
    print("The High Score is:",highscore)
except:
    highscore = 0

while z == 1:
    x = 50 + (random.random()*700)
    y = 50 + (random.random()*700)
    ball = Circle((x,y), 50)
    ball.fill = Color("Black")
    ball.draw(win)
    gamescore = Text((750,20),"Score: {}".format(str(score)))
    gamescore.fill = Color("Black")
    gamescore.draw(win)
    wait(0.5)
    ball.undraw()
    click = win.getMouse()
    if (x-50) <= click[0] <= (x+50) and (y-50) <= click[1] <= (y+50):
        gamescore.undraw()
        score = score + 10
    elif click[0] < (x-50) or click[1] < (y-50) or click[0] > (x+50) or click[1] > (y+50):
        z = 2
        win.setBackground(Color("black"))
        t = Text((370,400), "Game Over")
        t.fill = Color("White")
        strscore = str(score)
        tscore = Text((370,440), "Your Score: {}".format(strscore))
        tscore.fill = Color("lightblue")
        t.draw(win)
        tscore.draw(win)
        strhighscore = str(highscore)
        thighscore = Text((370, 420), "High Score: {}".format(strhighscore))
        thighscore.fill = Color("lightblue")
        thighscore.draw(win)
        print("Your Score Was:", score)

if score > int(highscore):
    f = open("spot.txt", "w")
    f.write(strscore)
    f.flush()
    f.close()
    print("Congrats! You made the High score!")
    ifhighscore = Text((370, 460), "Congrats! You made the High score!")
    ifhighscore.fill = Color("lightblue")
    ifhighscore.draw(win)
else:
    highscore = highscore
