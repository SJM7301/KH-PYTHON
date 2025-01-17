'''
Created on 2024. 12. 5.

@author: user
'''
def func1():
    global a;  # global을 사용해서 전역 변수로 바꿈
    a = 10;
    print("func1()에서 a값 %d" % a);

def func2():
    print("func2()에서 a값 %d" % a);

# 함수 변수
a = 20;  # 전역 변수

func1();
func2();