'''
Created on 2024. 12. 4.

@author: user
'''
hap = 0;
n = 1234;

while n < 4567:
    if n % 444 == 0:
        hap += n;
    n += 1;
    
print(hap);