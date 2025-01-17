'''
Created on 2024. 12. 9.

@author: user
'''
inFp = None;
inList, inStr = [], "";

inFp = open("C:/Temp/data1.txt", "r", encoding = "UTF-8");

inList = inFp.readlines();
print("inList 길이: ", len(inList));
count = 0;

for inStr in inList:
    count += 1;
    print(inStr, end = "");

print("\ncount = ", count);

inFp.close();