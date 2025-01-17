'''
Created on 2024. 12. 6.

@author: user
'''
from tkinter import *;
window = Tk();

window.title("냥이들 ^^");
window.geometry("500x300");

photo1 = PhotoImage(file = "images/GIF/cat.gif")
photo2 = PhotoImage(file = "images/GIF/cat2.gif")

label1 = Label(window, image = photo1);
label2 = Label(window, image = photo2);

label1.pack(side = LEFT);
label2.pack(side = LEFT);

window.mainloop();