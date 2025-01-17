'''
Created on 2024. 12. 5.

@author: user
'''
def base2(num):
    if (num < 2):
        print(numberStr[num], end="");
    else:
        base2(num // 2);
        print(numberStr[num % 2], end="");
        
def base8(num):
    if (num < 8):
        print(numberStr[num], end="");
    else:
        base8(num // 8);
        print(numberStr[num % 8], end="");
        
def base16(num):
    if (num < 16):
        print(numberStr[num], end="");
    else:
        base16(num // 16);
        print(numberStr[num % 16], end="");

numberStr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"];

number = int(input("10진수 입력 --> "));
print("\n2진수: ", end="");
base2(number);
print("\n8진수: ", end="");
base8(number);
print("\n16진수: ", end="");
base16(number);