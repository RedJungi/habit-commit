## 그림판 만들기 ##

from curses import window
import imp
from tkinter import *
from tkinter.colorchooser import *
from tkinter.simpledialog import *
from turtle import color, pencolor, width

from pip import main

# 함수 선언 부분 #
def mouseClik(event) :
  global x1, y1, x2, y2
  x1 = event.x
  y1 = event.y

def mouseDrop(event) :
  global x1, y1, x2, y2, penWidth, pencolor
  x1 = event.x
  y1 = event.y
  Canvas.create_line(x1, y1, x2, y2, width=penWidth, fill=pencolor)

def getColor() :
  global pencolor
  color = askcolor()
  pencolor = color[1]

def getWidth() :
  global penWidth
  penWidth = askinteger("선 두께", "선 두께(1~10)를 입력하세요", minvalue=1, maxvalue=10)

# 전역 변수 선언 부분 #
window = None
Canvas = None
x1, y1, x2, y2 = None, None, None, None
pencolor = 'black'
penWidth = 5

# 메인 코드 부분 #
if __name__=="__main__":
  window = Tk()
  window.title("그림판 비슷한 프로그램")
  Canvas = Canvas(window, height = 300, width = 300)
  Canvas.bind("<Button-1>", mouseClik)
  Canvas.bind("<ButtonRelease-1>", mouseDrop)
  Canvas.pack()

  mainMenu = Menu(window)
  window.config(menu = mainMenu)
  fileMenu = Menu(mainMenu)
  mainMenu.add_cascade(label="설정", menu = fileMenu)
  fileMenu.add_command(label="선 색상 선택", command = getColor)
  fileMenu.add_separator()
  fileMenu.add_command(label="선 두께 설정", command = getWidth)

  window.mainloop()