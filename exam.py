#연산자를 이용해 온도 단위를 변환하는 프로그램을 만들어 보세요
#섭씨온도 저장 변수 만듦, 화씨온도 = (섭씨온도*9/5)+32
#섭씨 온도와 화씨 온도를 다음과 같이 출력
#섭씨온도 : 30
#화씨 온도 : 86.0

celsius = int(input("섭씨온도를 입력하세요 >>"))
fahrenheit = float((celsius*9/5)+32)
result = round(fahrenheit,1)

print(f"섭씨 온도 : {celsius}\n화씨 온도 : {result}")

