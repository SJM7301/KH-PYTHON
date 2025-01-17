'''
Created on 2024. 12. 4.

@author: user
'''
import random;
'''
# 중복 시 더하기가 안됨
anum = [];
suma = 0;
bnum = [];
sumb = 0;

for i in range(0, 2):
    anum.append(random.randrange(1, 7));
    bnum.append(random.randrange(1, 7));
    
print("A의 주사위 숫자는", anum, "입니다.");
print("B의 주사위 숫자는", bnum, "입니다.");

for i in range(1, 7):
    if (i in anum):
        suma += i;
        
for j in range(1, 7):
    if (j in bnum):
        sumb += j;
        
print(suma);
print(sumb);
'''

num1, num2, num3, num4 = [0] * 4;

num1 = random.randrange(1, 7);
num2 = random.randrange(1, 7);
num3 = random.randrange(1, 7);
num4 = random.randrange(1, 7);

print("A의 주사위 숫자는 %d %d입니다." % (num1, num2));
print("B의 주사위 숫자는 %d %d입니다." % (num3, num4));

if ((num1 + num2) > (num3 + num4)):
    print("A가 이겼습니다.");
elif ((num1 + num2) < (num3 + num4)):
    print("B가 이겼습니다.");
else:
    print("둘이 비겼습니다.");