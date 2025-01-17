'''
Created on 2024. 12. 6.

@author: user
'''
from tkinter import *;
from time import *;
window = Tk();

# 전역 변수 선언
fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif",
             "jeju4.gif", "jeju5.gif", "jeju6.gif",
             "jeju7.gif", "jeju8.gif", "jeju9.gif"];

photoList = [None] * 9;
num = 0;

# 함수 선언
def clickNext():
    global num;
    num += 1;
    if (num > 8):
        num = 0;
    updateImage();

def clickPrev():
    global num;
    num -= 1;
    if (num < 0):
        num = 8;
    updateImage();

def updateImage():
    # 이미지 업데이트
    photo = PhotoImage(file = "images/GIF/" + fnameList[num]);
    pLabel.configure(image = photo);
    pLabel.image = photo;
    
    # 파일명 업데이트
    labelN.configure(text = fnameList[num]);

# 메인 코드
window.geometry("700x500");
window.title("사진 앨범 보기");

# 버튼 생성
btnPrev = Button(window, text = "<< 이전", command = clickPrev);
btnNext = Button(window, text = "다음 >>", command = clickNext);

# 초기 이미지 설정
photo = PhotoImage(file = "images/GIF/" + fnameList[0]);
pLabel = Label(window, image = photo);

# 파일명 표시 라벨
labelN = Label(window, text = fnameList[0]);

# 위치 배치
btnPrev.place(x = 250, y = 10);
btnNext.place(x = 400, y = 10);
pLabel.place(x = 15, y = 50);
labelN.place(x = 330, y = 10);

window.mainloop();