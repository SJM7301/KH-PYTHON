'''
Created on 2024. 12. 9.

@author: user
'''
# 변수 선언
i, dan = 0, 0; # 1.변수 선언 및 초기화

# 메인 코드
dan = int(input("단을 입력하세요 : ")); # 2.입력함수 사용 및 정수 형식 변환

for i in range(1, 10, 1): # 3.반목문 사용
    print("%d X %d = %2d" % (dan, i, (dan * i)));