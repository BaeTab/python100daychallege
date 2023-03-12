#5장 셀프체크
#시스템 오류로 일부 과목이 중복 신청되는 문제 발생 중복 과목을 없애는 프로그램을 작성하세요
#1. 신청과목은 리스트로 관리된다 / 2. 리스트에 같은과목이 2번 이상 포함된 경우 1개만 남기고 나머지는 삭제한다
#3. 출력시 신청 과목의 순서는 변경해도 괜찮다.
#리스트에 '자료구조 , 알고리즘 , 자료구조 , 운영체제' 를 넣었을때

academy_subject = ['자료구조', '알고리즘','자료구조','운영체제']
academy_subject = set(academy_subject)
academy_subject = list(academy_subject)
print(academy_subject)

#6.3실습문제: 택시 승객 수 구하기
#손님이 총 50명일 때 , 조건을 만족하는 총 탑승객 수 구하기
#1.손님별 운행 소요시간은 5~50분의 난수
#2.운행 소요시간 5~16분인 손님만 매칭한다.
#3.실행결과는 다음 형태로 출력하되. 매칭되면[o] 매칭되ㅑ지 않으면 []로 표시한다

from random import *

result = 0

for customer in range(1,51):
    driving_time = randint(5,51)
    
    if driving_time <=15:
        print(f"[o]{customer}번째 손님 (소요시간 : {driving_time}분)")
        result += 1
    else:
        print(f"[ ]{customer}번째 손님 (소요시간 : {driving_time}분)")

print(f"총 탑승객 : {result}")

#6장 셀프체크
#편의점에서 동일한 상품 2개를 구매하면 상품 1개를 무료로 제공하는 2+1 이벤트 진행 / 구매 상품수에 따라 가격을 계산하는 프로그램작성
#1.상품 1개의 가격은 1,000원
#2.고객은 3,6,9 처럼 항상 3의 배수에 해당하는 상품을 구매
#3.상품은 각각 스캔하며 한상품을 스캔할 때마다 2+1 상품입니다 를 출력

buy_num = int(input('몇개를 구매하시겠습니까? 3의배수로 입력하세요 > '))
total_price = int((buy_num/3)*2000)
for result in range(buy_num):
    print("2+1 상품입니다")
print(f"총 가격은 {total_price}원입니다.")