'''
Created on 2024. 12. 5.

@author: user
'''
def factoral(num):
    if (num <= 1):
        return num;
    else:
        return (num * factoral(num - 1));

print(factoral(4));