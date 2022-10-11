## 윈도프로그래밍 (체크버튼) ##

from operator import invert
from tabnanny import check
from tkinter import *
from tkinter import messagebox
window = Tk()

# 함수 선언 부분 #
def myFunc() :
  if check.get() == 0 :
    messagebox.showinfo("","체크버튼이 꺼졌어요.")
  else :
    messagebox.showinfo("","체크버튼이 켜졌어요.")
# 메인 코드 부분 #
check = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요", variable = check, command = myFunc)

cb1.pack()

window.mainloop()