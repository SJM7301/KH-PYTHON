'''
Created on 2024. 12. 5.

@author: user
'''
# 전역 변수 선언
coffee = 0; # 1.변수 선언 및 초기화 


# 함수 선언
def coffee_machine(button): # 2.함수 작성
    print("#1. 뜨거운 물을 준비한다.");
    print("#2. 종이컵을 준비한다.");
    
    if (button == 1):
        print("#3. 보통커피를 탄다.");
    elif (button == 2):
        print("#3. 설탕커피를 탄다.");
    elif (button == 3):
        print("#3. 블랙커피를 탄다.");
    print("#4. 물을 붓는다.");
    print("#5. 스푼으로 젓는다.");

# 메인 코드
coffee = int(input("어떤 커피 드릴까요?(1:보통, 2:설탕, 3:블랙) ")); # 3.입력함수 사용 및 coffee_machine함수 호출
coffee_machine(coffee);
print("손님~ 커피 여기 있습니다.");