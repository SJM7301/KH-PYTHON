'''
Created on 2024. 12. 9.

@author: user
'''
outFp = None;
outStr = "";

outFp = open("C:/Temp/data2.txt", "w", encoding = "UTF-8");

while (True):
    outStr = input("내용 입력: ");
    if outStr != "":
        outFp.writelines(outStr + "\n");
    else:
        break;

outFp.close();
print("---정상적으로 파일에 씀---");