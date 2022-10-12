from tkinter import *
from time import *

## 전역 변수 선언 부분 ##
fnameList = ["test1.gif", "test2.gif", "test3.gif", "test4.gif", "test5.gif",
"test6.gif", "test7.gif", "test8.gif", "test9.gif",]
photoList = [None] * 9
num = 0

## 함수 선언 부분 ##
def clickNext() :
    global num
    num += 1
    if num > 8 :
        num = 0
    photo = PhotoImage(file = "chapter10/gif/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

def clickPrev() :
    global num
    num -= 1
    if num < 0 :
        num = 8
    photo = PhotoImage(file = "chapter10/gif/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

## 메인 코드 부분 ##
window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clickNext)

window.bind("<Up>", clickNext)      # PageUp key click
window.bind("<Down>", clickPrev)    # PageDown key click

photo = PhotoImage(file = "chapter10/gif/" + fnameList[0])
pLabel = Label(window, image = photo)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x = 15, y = 50)

window.mainloop()