'''
Created on 2024. 12. 4.

@author: user
'''
oldList = ["짜장면", "탕수육", "군만두"];

# 얕은 복사(Shallow Copy)
# newList = oldList;

# 깊은 복사(Deep Copy)
# newList = oldList[:];

newList = oldList.copy();

print(newList);

oldList[0] = "짬뽕";
oldList.append("깐풍기");
print(newList);