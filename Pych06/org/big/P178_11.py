'''
Created on 2024. 12. 4.

@author: user
'''
hap = 0;

for n in range(3, 101):
    sosuYN = True;
    
    for i in range(2, n):
        if (n % i == 0):
            sosuYN = False;
    if (sosuYN):
        print(n, end=" ");