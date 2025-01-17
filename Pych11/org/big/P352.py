'''
Created on 2024. 12. 6.

@author: user
'''
# 입력 파일
inFp = None;

# 읽어온 문자열
inStr = "";

inFp = open("C:/Temp/data1.txt", "r", encoding = "UTF-8"); # r = 읽기 모드, encoding = "UTF-8" -> 유니코드로 변환

inStr = inFp.readline();
print(inStr, end = "");
inFp.close();