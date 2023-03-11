# Day4 Exam1
# 이름 입력해서 랜덤으로 뽑기

# Split string method
names_string = input("Give me everybody's names, separated by a comma.")
names = names_string. split(", ") #입력받은 문자열을 , 로 구분하여 list 로 저장
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random #랜덤 모듈 임포트

random_index = random.randint(0, len(names) - 1) 
#len(name)은 5로 나오기때문에 -1을a 해서 리스트에서 뽑을수 있게함)
random_name = names[random_index]
#name 의 리스트에서 0~4 로 나온 랜덤수를 넣음
print(f"{random_name} is going to buy the meal today!") #출력


#Day4 Exam2
#입력받은 값 행,열 따져 x 표시 하기 

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]  			#3개의 리스트를 하나로 병합 
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

position_id = int(position)  		#입력받은값 변수에 저장

row = position_id % 10 -1			#변수 / 10 하면 나머지가 1~3으로 나오니 0~2로 나오게 -1해줌
column = int(position_id / 10) -1	#변수 / 10 하면 몫이 1~3으로 나오니 0~2로 나오게 =1 해줌

map[row][column] =  "X"				# map의 row , column 에 각값을 넣어 해당위치를 X로 바꿈

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

#Day4 final Project
#가위바위보 게임

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

user = int(input("1.가위 ,  2.바위 , 3.보 / 선택해주세요 >> "))
computer = random.randint(1,3)


if user == 1:
  print("user\n"+scissors)
  if computer == 2:
    print("computer\n"+rock+"\nComputer win!")
  elif computer == 3:
    print("computer\n"+paper+"\nUser win")
  else:
    print("computer\n"+scissors+"\nDraw")

if user == 2:
  print("user\n"+rock)
  if computer == 2:
    print("computer\n"+rock+"\nDraw!")
  elif computer == 3:
    print("computer\n"+paper+"\nComputer win")
  else:
    print("computer\n"+scissors+"\nUser win")

if user == 3:
  print("user\n"+paper)
  if computer == 2:
    print("computer\n"+rock+"\nUser win")
  elif computer == 3:
    print("computer\n"+paper+"\nDraw!")
  else:
    print("computer\n"+scissors+"\nComputer win")