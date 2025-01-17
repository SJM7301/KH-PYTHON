'''
Created on 2024. 12. 4.

@author: user
'''
aa = [];

for i in range(0, 10): # aa = [10개의 배열];
    aa.append(0);

hap = 0;

for i in range(0, 10):
    aa[i] = int(input(str(i + 1) + "번째 숫자: "));
    hap += aa[i];

print("합계 ==> %d" % hap);