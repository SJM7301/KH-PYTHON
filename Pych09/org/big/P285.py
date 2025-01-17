'''
Created on 2024. 12. 5.

@author: user
'''
'''
def outFunc(v1, v2):
    def inFunc(num1, num2):
        return num1 + num2;
    return inFunc(v1, v2);

print(outFunc(10, 20));
'''

def hap(num1, num2):
    res = num1 + num2;
    return res;

print(hap(10, 20));