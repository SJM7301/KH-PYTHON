'''
Created on 2024. 12. 9.

@author: user
'''
inFp, outFp = None, None;
inStr = "";

inFp = open("C:/windows/notepad.exe", "rb");
outFp = open("C:/Temp/notepad.exe", "wb");

while (True):
    inStr = inFp.read(1);
    if (not inStr):
        break;
    outFp.write(inStr);

inFp.close();
outFp.close();

print("---이진 파일이 정상적으로 복사되었음---");