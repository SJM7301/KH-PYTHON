'''
Created on 2024. 12. 4.

@author: user
'''
list1 = [];
list2 = [];
value = 0;

for i in range(0, 4):
    for j in range(0, 5):
        list1.append(value);
        value += 3;
    list2.append(list1);
    list1 = [];
    
for i in range(0, 4):
    for j in range(0, 5):
        print("%3d" % list2[i][j], end=" ");
    print("");  # 줄바꿈용