'''
Created on 2024. 12. 4.

@author: user
'''
i, k = 0, 0;

for i in range(2, 10, 1):
    print("## %d단 ##" % i);
    
    for k in range(1, 10, 1):
        print("%d X %d = %d" % (i, k, i * k));
    print("");