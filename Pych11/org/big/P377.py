'''
Created on 2024. 12. 9.

@author: user
'''
myStr = "파이썬은 재미 있어요. 파이썬만 매일매일 공부하고 싶어요.^^";
strPosList = [];
index = 0;

while (True):
    try:
        index = myStr.index("파이썬", index);
        strPosList.append(index);
        index = index + 1; # 다음 위치 부터 찾음
    except:
        break;
print("파이썬 글자 위치 --> ", strPosList);