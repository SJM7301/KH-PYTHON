'''
Created on 2024. 12. 5.

@author: user
'''


def func1():
    a = 10;  # 지역변수
    print("func1()에서 a값 %d" % a);

    
def func2():
    print("func2()에서 a값 %d" % a);

# 전역 변수
a = 20;

func1()
func2()