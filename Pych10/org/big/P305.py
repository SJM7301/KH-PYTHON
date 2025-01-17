'''
Created on 2024. 12. 6.

@author: user
'''
from tkinter import *;
window = Tk();

button1 = Button(window, text = "파이썬 종료", fg = "red", command = quit);

button1.pack();

window.mainloop();