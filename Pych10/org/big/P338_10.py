'''
Created on 2024. 12. 6.

@author: user
'''

'''
Created on 2024. 12. 6.

@author: user
'''
from tkinter import *;
from tkinter.filedialog import *;

def func_zoomIn(event = None):
    global photo, value;
    value += 1;
    photo = photo.zoom(value, value);
    pLabel.configure(image = photo);
    pLabel .image = photo;

def func_zoomOut(event = None):
    global photo, value;
    value += 1;
    photo = photo.subsample(value, value);
    pLabel.configure(image = photo);
    pLabel .image = photo;

window = Tk();

# 함수 선언
def func_open():
    global photo;
    filename = askopenfilename(parent = window, filetypes = (("GIF파일", "*.gif"), ("모든 파일", "*"))); 
    photo = PhotoImage(file = filename);
    
    # 이미지 크기
    width = photo.width();
    height = photo.height();
    
    # 이미지 색상
    for x in range(width):
        for y in range(height):
            r, g, b = photo.get(x, y);
            gray = int((r + g + b) // 3);
            photo.put("#%02x%02x%02x" % (gray, gray, gray), (x, y));
    
    pLabel.configure(image = photo);
    pLabel.image = photo;

def func_exit():
    window.quit();
    window.destroy();

# 메인 코드
window.geometry("500x500");
window.title("명화 감상하기");

value = 1;

photo = PhotoImage();
pLabel = Label(window, image = photo);
pLabel.pack(expand = 1, anchor = CENTER);

mainMenu = Menu(window);
window.config(menu = mainMenu);
fileMenu = Menu(mainMenu);
sizeMenu = Menu(mainMenu);

mainMenu.add_cascade(label = "파일", menu = fileMenu);
fileMenu.add_command(label = "파일 열기", command = func_open);
fileMenu.add_separator();
fileMenu.add_command(label = "프로그램 종료", command = func_exit);

mainMenu.add_cascade(label = "크기 조절", menu = sizeMenu);
sizeMenu.add_command(label = "확대", command = func_zoomIn);
sizeMenu.add_command(label = "축소", command = func_zoomOut);

window.bind("<Up>", func_zoomIn);
window.bind("<Down>", func_zoomOut);
window.bind("<Button-1>", func_zoomIn);
window.bind("<Button-3>", func_zoomOut);

window.mainloop();