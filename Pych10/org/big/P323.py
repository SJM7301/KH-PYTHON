'''
Created on 2024. 12. 6.

@author: user
'''
from tkinter import *;
window = Tk();

# 메뉴 자체
mainMenu = Menu(window);
window.config(menu = mainMenu);

# 메뉴 만들기
fileMenu = Menu(mainMenu);
mainMenu.add_cascade(label = "파일", menu = fileMenu);

# 메뉴바 안에 들어갈 속성
fileMenu.add_command(label = "열기");

# 메뉴 사이에 구분선 추가
fileMenu.add_separator();

# 메뉴바 안에 들어갈 속성
fileMenu.add_command(label = "종료");

window.mainloop();