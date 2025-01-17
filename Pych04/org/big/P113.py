'''
Created on 2024. 12. 3.

@author: user
'''
a = 100;
result = 0;
i = 0;

for i in range(1, 5):
    result = a << i;
    print("%d << %d = %d" % (a, i, result)); # 좌 시프트는 증가연산

for i in range(1, 5):
    result = a >> i;
    print("%d >> %d = %d" % (a, i, result)); # 우 시프트는 감소연산