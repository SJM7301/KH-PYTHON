'''
Created on 2024. 12. 5.

@author: user
'''
inStr = "IT_CookBook_Python";
outStr = "";

for i in range(0, len(inStr)):
    if (i % 2 == 0):
        outStr += inStr[len(inStr) - (i + 1)];
    else:
        outStr += "#";

print("원본 내용 --> ", inStr);
print("변경 내용 --> ", outStr);