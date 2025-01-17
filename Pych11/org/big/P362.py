'''
Created on 2024. 12. 9.

@author: user
'''
# 변수 선언
inFp, outFp = None, None;
inStr, outStr = "", "";
i, secu = 0, 0;

# 메인 코드
secuYN = input("1.암호화 2.암호 해석 중 선택: ");
inFname = input("입력 파일명을 입력하세요: ");
outFname = input("출력 파일명을 입력하세요: ");

if (secuYN == "1"):
    secu = 100;
elif (secuYN == "2"):
    secu = -100; # -100의 -는 부호

inFp = open(inFname, "r", encoding = "UTF-8");
outFp = open(outFname, "w", encoding = "UTF-8");

while (True):
    inStr = inFp.readline();
    if (not inStr):
        break;
    
    outStr = "";
    for i in range(0, len(inStr)):
        ch = inStr[i];
        chNum = ord(ch);
        chNum = chNum + secu;
        ch2 = chr(chNum);
        outStr = outStr + ch2;
    
    outFp.write(outStr);

outFp.close();
inFp.close();
print("%s --> %s 변환 완료" % (inFname, outFname));