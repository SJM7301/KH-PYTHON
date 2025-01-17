'''
Created on 2024. 12. 5.

@author: user
'''
def dic_func(**para):
    for k in para.keys():
        print("%s --> %d명입니다." % (k, para[k]));

dic_func(트와이스 = 9, 소녀시대 = 7, 걸스데이 = 4, 블랙핑크 = 4);