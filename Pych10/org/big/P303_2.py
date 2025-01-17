'''
Created on 2024. 12. 6.

@author: user
'''
from tkinter import *;
window = Tk();

window.title("레이블");
window.geometry("400x100");

label1 = Label(window, text = "COOKBOOK~~Python을");
label2 = Label(window, text = "열심히", font = ("궁서체", 30), fg = "blue")
label3 = Label(window, text = "공부중입니다.", bg = "magenta", width = 20, height = 5, fg = "white", anchor = SE);

label1.pack();
label2.pack();
label3.pack();

window.mainloop();