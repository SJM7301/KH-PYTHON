'''
Created on 2024. 12. 5.

@author: user
'''
inStr = "파이썬 ### CookBook $$$ @@@ 열공중 1234";
outStr = ""; 

for i in range(0, len(inStr)):
    if (inStr[i].isalpha() == True):
        outStr += inStr[i];

print("문자열--> ", inStr);
print("한글/영문자만 남김--> " + outStr);