'''
Created on 2024. 12. 4.

@author: user
'''

'''
hap = 0;
a, b = 0, 0;

while True:
    a = input("더할 첫 번째 수를 입력하세요: ");
    if (a == "$"):
        break;
    
    b = int (input("더할 첫 번째 수를 입력하세요: "));

    hap = int(a) + b;
    print("%d + %d = %d" % (int(a), b, hap));

print("$를 입력해 본복문을 탈출했습니다.");
'''

hap = 0;
a, b = 0, 0;

while True:
    a = input("더할 첫 번째 수를 입력하세요: ");
    if (a == "$"):
        break;

    b = int (input("더할 첫 번째 수를 입력하세요: "));

    a = int(a);
    hap = a + b;
    print("%d + %d = %d" % (a, b, hap));

print("$를 입력해 본복문을 탈출했습니다.");