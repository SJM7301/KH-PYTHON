'''
Created on 2024. 12. 9.

@author: user
'''
from tkinter import *;

# 변수 선언
window = None; 
canvas = None;
XSIZE, YSIZE = 256, 256; # 변수를 대문자로 지정하면 상수의 의미를 가진다.

window = Tk();

canvas = Canvas(window, height = XSIZE, width = YSIZE);

canvas.pack();
window.mainloop();