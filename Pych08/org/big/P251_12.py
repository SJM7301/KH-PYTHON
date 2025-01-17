'''
Created on 2024. 12. 5.

@author: user
'''
inStr, outSrt, numStr, lowerStr, upperStr, hanStr, etcStr = [""] * 7;
inStr = input("문자열을 입력하세요: "); # IT CookBook 파이썬을 365일 공부하고 있습니다. ^__^
outStr = ""; 

for i in inStr:
    if (ord(i) >= ord("A") and ord(i) <= ord("Z")):
        upperStr += i;
    elif (ord(i) >= ord("a") and ord(i) <= ord("z")):
        lowerStr += i;
    elif (ord(i) >= ord("0") and ord(i) <= ord("9")):
        numStr += i;
    elif (ord(i) >= ord("가") and ord(i) <= ord("힣")):
        hanStr += i;
    else:
        etcStr += i;
        
print("대문자: ", upperStr);
print("소문자: ", lowerStr);
print("숫자: ", numStr);
print("한글: ", hanStr);
print("기타문자: " , etcStr);