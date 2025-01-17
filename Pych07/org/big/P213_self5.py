'''
Created on 2024. 12. 4.

@author: user
'''
animals = {"닭":"병아리",
           "개":"강아지",
           "곰":"능소니",
           "고등어":"고도리",
           "명태":"노가리",
           "말":"망아지",
           "호랑이":"개호주"};
           
while(True):
    animal = input(str(list(animals.keys())) + "중 새끼 이름을 알고 싶은 동물은?");
    
    if (animal in animals):
        print("<%s>의 새끼는 <%s>입니다." % (animal, animals.get(animal)));
    elif (animal == "끝"):
        break;
    else:
        print("말씀하신 동물이 없습니다. 리스트를 다시 확인해 보세요.");