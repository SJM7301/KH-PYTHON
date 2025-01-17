'''
Created on 2024. 12. 4.

@author: user
'''
tt = ( (1, 2, 3),
       (4, 5, 6),
       (7, 8, 9));

for i in range(0, 3):
    for j in range(0, 3):
        print("%3d" % tt[i][j], end="");
    print("");