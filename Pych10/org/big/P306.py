'''
Created on 2024. 12. 6.

@author: user
'''
from tkinter import *;
from tkinter import messagebox;
window = Tk();

# 함수 선언
def myFunc():
    messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠? ^^");

# 메인 코드
window.title("tk");

photo = PhotoImage(file = "images/GIF/dog2.gif");

button1 = Button(window, image = photo, command = myFunc);

button1.pack();

window.mainloop();