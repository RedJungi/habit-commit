## 리스트를 활용해 화면 밖으로 나가는 거북이 프로그램 ##
from tkinter.tix import TList
import turtle
import random

# 전역 변수 선언 부분 #
myTurtle, tX, tY, tColor, tSize, tShape = [None] * 6
shapelist = []
playerTurtles = []
swidth, sheight = 500, 500

# 메인 코드 부분 #
if __name__=="__main__":
  turtle.title('거북 리스트 활용')
  turtle.setup(width = swidth + 50, height = sheight + 50)
  turtle.screensize(swidth, sheight)

  shapelist = turtle.getshapes()
  for i in range(0, 100) :
    random.shuffle(shapelist)
    myTurtle = turtle.Turtle(shapelist[0])
    tX = random.randrange(-swidth / 2, swidth / 2)
    tY = random.randrange(-sheight / 2, sheight / 2)
    r = random.random(); g = random.random(); b = random.random()
    tSize = random.randrange(1, 3)
    playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b])

    for tlsit in playerTurtles :
      myTurtle = tlsit[0]
      myTurtle.color((tlsit[4], tlsit[5], tlsit[6]))
      myTurtle.pencolor((tlsit[4], tlsit[5], tlsit[6]))
      myTurtle.turtlesize(tlsit[3])
      myTurtle.goto(tlsit[1], tlsit[2])
      turtle.done()