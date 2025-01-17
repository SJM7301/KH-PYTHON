'''
Created on 2024. 12. 6.

@author: user
'''
from tkinter import *;
from tkinter import messagebox;
window = Tk();

# 함수 선언
def func_open():
    messagebox.showinfo("메뉴선택", "열기 메뉴를 선택함");

def func_exit():
    window.quit();
    window.destroy();

# 메뉴 자체
mainMenu = Menu(window);
window.config(menu = mainMenu);

# 메뉴 만들기
fileMenu = Menu(mainMenu);
mainMenu.add_cascade(label = "파일", menu = fileMenu);

# 메뉴바 안에 들어갈 속성
fileMenu.add_command(label = "열기", command = func_open);

# 메뉴 사이에 구분선 추가
fileMenu.add_separator();

# 메뉴바 안에 들어갈 속성
fileMenu.add_command(label = "종료", command = func_exit);

window.mainloop();