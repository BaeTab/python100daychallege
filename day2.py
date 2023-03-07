print("hello"[4]) # o 를 출력

#integer
123456

#float
3.14159

#boolean
True
False

#Type converting
num_char = len(input("What is your name?"))
print(type(num_char)) # int
new_num_char = str(num_char)
print ( "your name has"+ new_num_char+ " characters")

a = str(123)
print(type(a))

#두 숫자를 입력받아 덧셈(int)형식으로 출력
a = (input("Type a two digit number >> " ))
new_a = int(a[0])
new_a2 = int(a[1])

print(new_a+new_a2)

#bmi calculator
height = float(input("키를 입력해주세요 >"))
weight = int(input("몸무게를 입력해주세요 >"))

Bmi =  weight / (height*height)
print(int(Bmi))

#round ( 8/3 , 2) 소숫점 2자리 까지 표시 나머지 반올림 가능

#f-String ex)print(print(f"your score {score} , your height is{height} , you are winning is {isWinning}")

#수명이 90세 까지일때 몇일 , 몇주 , 몇달 이 남았나 보여주기 ( 현재 나이 입력 받음)
age = int(input ("현재 나이를 입력해 주세요 > "))

days = (age * int(365))
weeks = (age * int(52))
month = (age * int(12))

print(f"당신의 수명은{days}일 , {weeks}주, {month}개월 남았습니다")

#tip calculator
#1. total bill 얼마 ? / 2. 팁 비율 (10,12,15% 중 선택) / 3. 몇명이서 나눌꺼임?

print("N빵용 팁 계산기 입니다.")
total_bill = float(input("계산 금액이 얼마 입니까? : $"))
tip_with_bill = float(input("몇퍼센트의 팁을 줄껀가요? 10,12,15% 중 택1\n숫자만 입력하세요 > ")) *0.01 + total_bill
split_people = int(input("몇분이서 나누어 계신하시나요 ? > "))

pay = round(tip_with_bill/split_people,2)

print(f"1인당 결제금액은 ${pay} 입니다")