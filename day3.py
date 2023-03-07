#Day3 Exam1
#입력받은 값이 홀수인지 , 짝수인지 판별
num = int(input("숫자를 입력해주세요 >"))
if num%2==0:
    print("짝수입니다!")
else:
    print("홀수입니다!")

#Day3 Exam2
#Bmi calculatpr v2.0
height = float(input("키를 입력해주세요(m 단위) >"))
weight = float(input("몸무게를 입력해주세요(kg단위) >"))
bmi = round(weight / height ** 2)

if bmi < 18.5 :
    print("저체중 입니다")
elif bmi <25 :
    print("정상체중 입니다")
elif bmi <30:
    print("과체중 입니다")
elif bmi <35:
    print("비만 입니다")
else:
    print("고도비만 입니다")

#Day3 Exam3
#윤년 계산하기
#윤년 조건 /년도%4 =0 , 년도%400=0 윤년 / 년도%4=0 ,년도%100=0,년도%400 = 0 윤년/
#평년 조건 /년도%4 =0 , 년도%100=0 년도%400!=0 /년도%4 !=0

years = int(input("년도를 입력해주세요 > "))

# 본인 작성 코드
# if years%4==0:
#     if years%100==0:
#         if years%400==0:
#             print("윤년입니다")
# elif years%4==0:
#     if years%100!=0:
#         if years%400==0:
#             print("윤년입니다")
# elif years%4!=0:
#     print("평년입니다")
# elif years%4==0:
#     if years%100==0:
#         if years%400!=0:
#             print("평년입니다")
# else:
#     print("평년입니다")

#정답코드

if years % 4 == 0:
    if years % 100== 0:
        if years % 400 == 0:
            print("윤년입니다")
        else:
            print("평년입니다")
    else:
        print("윤년입니다")            
else:
    print("평년입니다")
        
        
# #Day3 Exam4
# #피자가격 계산하기 feat.토핑추가
# #S:$15 , M:$20, L:$25 / 페퍼로니 추가 S:+$2 M,L:+$3  / 치즈추가 +$1

# 내가 쓴 코드
# size_info = str(input("사이즈를 입력해주세요 S , M , L >> "))
# add_pepperoni = str(input("페퍼로니를 추가하시겠습니까? Y,N >> "))
# add_cheese = str(input("치즈를 추가하시겠습니까? Y,N >>"))

# bill = 0

# if size_info == "S":
#     bill +=15
#     if add_pepperoni == "Y":
#         bill += 2
#     else:
#         bill += 0
#     if add_cheese == "Y":
#         bill += 1
#     else:
#         bill += 0
#     print(f"최종가격은 ${bill} 입니다")
    
# elif size_info =="M":
#     bill +=20
#     if add_pepperoni == "Y":
#         bill += 3
#     else:
#         bill += 0
#     if add_cheese == "Y":
#         bill += 1
#     else:
#         bill += 0
#     print(f"최종가격은 ${bill} 입니다")
    
# elif size_info =="L":
#     bill +=25
#     if add_pepperoni == "Y":
#         bill += 3
#     else:
#         bill += 0
#     if add_cheese == "Y":
#         bill += 1
#     else:
#         bill += 0
#     print(f"최종가격은 ${bill} 입니다")

# 정답코드

size_info = str(input("사이즈를 입력해주세요 S , M , L >> "))
add_pepperoni = str(input("페퍼로니를 추가하시겠습니까? Y,N >> "))
add_cheese = str(input("치즈를 추가하시겠습니까? Y,N >>"))

bill = 0

if size_info == "S":
    bill += 15
elif size_info == "M":
    bill += 20
elif size_info == "L":
    bill += 25

if add_pepperoni =="Y":
    if size_info =="S":
        bill += 2
    else:
        bill += 3       
if add_cheese =="Y":
    bill+=1

print(f"최종가격은 ${bill} 입니다!")


#Day3 Exam5 번역문제로 패스함. 대충 이름을 2개 입력받고 나오는 알파벳중 특정글자가 몇개 들어있나 세어서 사랑점수를 확인한다는 내용
#Agella.lower() / 대문자를 소문자로 바꿔줌  , Agella.count("l") 알파벳중 l 이 몇개 들어가있다 세어줌 이런걸로 계산


#Day3 final project 보물섬 게임 만들기

print('''                                         {'{
                                         /   '.
                                       _/     _}
    쭝꿔                          __ __}      /
                                (  `        (
                          /'\____\          /
                         :                  |
                         /                  |
                        /                 _/
                  __.-='     DPRK        /
              .-='                   .-='
          .-='                 _.--='
         (                   .'
          \=._               }
              '-._          (
                 (           '=-.
                 / 북한           \
                (_ *              \
             _.='\\                \
            ;                       }         SEA OF
YELLOW      \__         _  _      .'\         ROK
 SEA         " \_ _ . -      - . -   \
                \                     \
              ,=.\ * 서울               \
             {_.                        }
              :`{                       |
                /                       /
                }                      .
                \           ROK        |
               _]                     <_.
               ',                       /
               /                       /
               \                _.____/
                }  _____.-.--=\{ /}
                \/" ,_}   \,      `


               __,=-.
dew           {__.--'   <보물섬                            \n\n''')

print("보물섬 게임을 시작합니다 , 선택은 한번 뿐 이니 신중하게 결정해주세요.")
lorr = str(input("보물섬에 도착했습니다. 양갈래 길이 나오네요. 왼쪽 또는 오른쪽 선택해주세요 >> "))
if lorr == "오른쪽":
    sorw = str(input("왼쪽엔 함정이 있었네요. 잘 선택하셨습니다. 앞에 바다가 있는데 수영 또는 대기 선택해주세요 >> "))
    if sorw == "대기":
        door = str(input("파도가 거새 수영을 했다면 위험했을껍니다. 둘러보니 문이 세개가 있습니다. 빨강,노랑,파랑 문중 어떤문을 들어가시겠습니까? >>"))
        if door =="노랑":
            print("축하합니다! 보물을 발견했습니다! 당신은 부자에요!")
        else:
            print("문을 열자마자 괴물 수백마리가 튀어나와서 공격당해 사망했습니다.")
    else:
        print("바다에 뛰어들었지만 크라켄을 만나 공격당해 사망했습니다.")
else:
    print("왼쪽 길에 들어서는 순간 함정에 빠져 사망했습니다.")
    


