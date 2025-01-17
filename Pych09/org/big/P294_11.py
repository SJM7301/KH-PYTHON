'''
Created on 2024. 12. 5.

@author: user
'''
def addNumber(num):
    if (num <= 1):
        return 1;
    else:
        return num + addNumber(num-1);

print(addNumber(100));