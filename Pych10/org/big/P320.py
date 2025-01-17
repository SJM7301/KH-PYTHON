'''
Created on 2024. 12. 6.

@author: user
'''
from tkinter import *;
from tkinter import messagebox;
window = Tk();

# 함수 선언
def keyEvent(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키: " + chr(event.keycode));

# 메인 코드
window.bind("<Key>", keyEvent);

window.mainloop();