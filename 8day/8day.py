## 맘대로 다니는 거북이 프로그램 ##

from ast import Break
import turtle
import random

# 전역 변수 선언 부분 #

swidth, sheight, pSize, exitCount = 300, 300, 3, 0
r, g, b, angle, dist, curX, curY = [0] * 7

# 메인 코드 부분 #
turtle.title('거북이가 맘대로 다니기')
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.setup(width = swidth + 30, height = sheight + 30)
turtle.sceensize(swidth, sheight)

while True :
  r = random.random()
  g = random.random()
  b = random.random()
  turtle.pencolor((r, g, b))

  angle = random.randrange(0, 360)
  dist = random.randrange(1, 100)
  turtle.left(angle)
  turtle.forward(dist)
  curX = turtle.xcor()
  curY = turtle.ycor()

  if (-swidth / 2 <= curX and curX <= swidth / 2) and (-swidth / 2 <= curY and curY <=
  sheight / 2):
    pass
else :
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

    exitCount += 1
    if exitCount >= 5 :
      Break 
   
turtle.done()

