# Day5 Exam2 
# 입력값 중 가장 높은 값 찾기

student_score = input("점수를 입력해주세요 (띄어쓰기로 구분) >> ").split()   #split 으로 띄어쓰기 구분해서 잘라줌
for i in range(0, len(student_score)):                             
    student_score[i] = int(student_score[i])                        #student_score 의 0부터~len만큼 반복하여
                                                                    #int값의 리스트를 작성

highest_score = 0
for score in student_score:
    if score > highest_score:                                       #조건이 True면 highest_score에 값 저장
        highest_score = score                                       #fals면 저장하지 않고 반복문으로 돌아감
    
print(f"최고점수는 {highest_score}점 입니다")

# Day5 Exam3
# 1~100까지의 모든 짝수의 합 (for range 문 이용)

result = 0
for i in range(2,101,2):
    result += i
print(f"모든 짝수의 합은 {result}")

result2 = 0
for j in range(1,101):
    if j%2 == 0:
        result2 += j
print(f"모든 짝수의 합은 {result2}")


# Day5 Exam4
# FizzBuzz 게임
# 3으로 나눌수있는 숫자일땐 Fizz , 5로 나눌수 있는 숫자일땐 Buzz 출력 , 3 5모두 나눌수있음 FizzBuzz
# (미국 아동용 게임이라고 한다 우리나라 369 비슷한 ㅋ)

for number in range(1,100):
    if number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    elif number%5==0 and number%3==0:
        print("FizzBuzz")
    else:
        print(number)
        
        # Day5 Fianl Project
# 패스워드 만들기 아래는 미리 만들어져있던 리스트
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)
# print(password)

#Hard Level
password_list = []          #최종 만들어질 패스워드의 리스트

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))  #letter에서 랜덤으로 초이스된 문자열을 리스트에 가장 뒤에 추가  (입력받은값까지) 

for char in range(1, nr_symbols + 1):           
  password_list += random.choice(symbols)       #마찬가지

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)       #마찬가지

print(password_list)
random.shuffle(password_list)                   #만들어진 리스트 섞어줌
print(password_list)                            #최종

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")