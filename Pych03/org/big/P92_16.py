'''
Created on 2024. 12. 3.

@author: user
'''
str = input("글자 입력: ");

if("0" <= str and str <= "1"):
    print("2진수 또는 8진수 또는 10진수 또는 16진수 입니다.");
elif ("0" <= str and str <= "7"):
    print("8진수 또는 10진수 또는 16진수 입니다.");
elif("0" <= str and str <= "9"):
    print("10진수 또는 16진수 입니다.");
elif("a" <= str and str <= "f" or "A" <= str and str <= "F"):
    print("16진수 입니다.");
else:
    print("숫자가 아닙니다.")