'''
Created on 2024. 12. 6.

@author: user
'''
from tkinter import *;
from random import *;
window = Tk();

# 전역 변수 선언
btnList = [None] * 9;
fnameList = ["honeycomb.gif", "icecream.gif", "jellybean.gif",
             "kitkat.gif", "lollipop.gif", "marshmallow.gif",
             "nougat.gif", "oreo.gif", "pie.gif"];

photoList = [None] * 9;

i, k, xPos, yPos, num = [0] * 5;

# 메인 코드
window.geometry("210x210");

shuffle(fnameList);

for i in range(0, 9):
    photoList[i] = PhotoImage(file = "images/GIF/" + fnameList[i]);
    btnList[i] = Button(window, image = photoList[i]);

for i in range(0, 3):
    for j in range(0, 3):
        btnList[num].place(x = xPos, y = yPos);
        num += 1;
        xPos += 70;
    xPos = 0;
    yPos += 70;

window.mainloop();