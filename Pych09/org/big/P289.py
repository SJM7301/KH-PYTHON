'''
Created on 2024. 12. 5.

@author: user
'''
def genFunc(num):
    for i in range(0, num):
        yield i;
        print("제너레이터 진행 중");

print(list(genFunc(5)));

for data in genFunc(5):
    print(data);