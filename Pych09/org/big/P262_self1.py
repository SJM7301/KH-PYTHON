'''
Created on 2024. 12. 5.

@author: user
'''
# 전역 변수 선언
coffee = 0;


# 함수 선언
def coffee_machine(button):
    print("#1. (자동으로) 뜨거운 물을 준비한다.");
    print("#2. (자동으로) 종이컵을 준비한다.");
    
    if (button == 1):
        print("#3. (자동으로) 아메리카노를 탄다.");
    elif (button == 2):
        print("#3. (자동으로) 카페라떼를 탄다.");
    elif (button == 3):
        print("#3. (자동으로) 카푸치노를 탄다.");
    elif (button == 4):
        print("#3. (자동으로) 에스프레소를 탄다.");
    else:
        print("1~4 숫자 중 선택해주세요.");
    print("#4. (자동으로) 물을 붓는다.");
    print("#5. (자동으로) 스푼으로 젓는다.");


coffee = int(input("로제씨, 어떤 커피 드릴까요?(1:아메리카노, 2:카페라떼, 3:카푸치노, 4:에스프레소) "));
coffee_machine(coffee);
print("로제씨~ 커피 여기 있습니다.");
print();

coffee = int(input("리사씨, 어떤 커피 드릴까요?(1:아메리카노, 2:카페라떼, 3:카푸치노, 4:에스프레소) "));
coffee_machine(coffee);
print("리사씨~ 커피 여기 있습니다.");
print();

coffee = int(input("지수씨, 어떤 커피 드릴까요?(1:아메리카노, 2:카페라떼, 3:카푸치노, 4:에스프레소) "));
coffee_machine(coffee);
print("지수씨~ 커피 여기 있습니다.");
print();

coffee = int(input("제니씨, 어떤 커피 드릴까요?(1:아메리카노, 2:카페라떼, 3:카푸치노, 4:에스프레소) "));
coffee_machine(coffee);
print("제니씨~ 커피 여기 있습니다.");
print();