import random
import time

print("원하는 사람이나 번호를 적습니다")
name_list = []

name = input("값 : ")
name_list.append(name)
print("만약에 멈추고 결과를 보고 싶다면 n을 눌러주세요")
while True:
    yn = input("y/n? : ")
    if yn == 'y':
        name = input("값 : ")
        name_list.append(name)
    elif yn == 'n':
        choice = random.choice(name_list)
        print("결과 : ",choice)
        time.sleep(3)
        break
    else:
        print("잘못된 단어입니다")






