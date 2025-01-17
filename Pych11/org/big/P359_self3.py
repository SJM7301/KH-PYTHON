'''
Created on 2024. 12. 9.

@author: user
'''
import os;

outFp = None;
fName, outStr = "", "";

fName = input("파일명을 입력하세요: ");

if (os.path.exists(fName)):
    outFp = open(fName, "w", encoding = "UTF-8");

    while (True):
        outStr = input("내용 입력: ");
        if outStr != "":
            outFp.writelines(outStr + "\n");
        else:
            break;
    
    outFp.close();
    print("---정상적으로 파일에 씀---");
else:
    print("파일이 없습니다.");