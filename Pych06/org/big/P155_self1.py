'''
Created on 2024. 12. 4.

@author: user
'''
i, hap = 0, 0;

for i in range(0, 101, 7):
    hap += i;
    
print("0과 100사이에 있는 7의 배수 합계: %d" % hap);