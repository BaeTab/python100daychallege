#Day7 Project 
#HANGMAN 게임 만들기

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]  #정답 리스트
chosen_word = random.choice(word_list)      #정답중 한개를 랜덤으로 선택
word_length = len(chosen_word)              #선택된 정답의 문자열길이

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6   #목숨 6개

#Testing code
print(f'Pssst, the solution is {chosen_word}.') #테스트 코드임 정답 보여줌

#Create blanks
display = []        #빈 리스트 생성
for _ in range(word_length):
    display += "_"  #정답의 문자열 길이 만큼 "_" 생성

while not end_of_game:  #게임이 끝나지 않았으면 반복
    guess = input("Guess a letter: ").lower() #문자 묻는 인풋

    #Check guessed letter
    for position in range(word_length): # 정답의 문자열 길이 만큼 반복
        letter = chosen_word[position]  # letter 에 정답 문자열 포지션 저장
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:     # 입력한 문자가 letter 에 있을때
            display[position] = letter  #  디스플레이 포지션에 넣음

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word: #입력한 문자가 정답안에 없을때
        lives -= 1      #목숨 -1
        if lives == 0:  #목숨이 0이 되면
            end_of_game = True #end_of_game 이 true로 바뀜 = while반복문 끝남
            print("You lose.")  # 졌다고 출력

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}") 

    #Check if user has got all letters.
    if "_" not in display:  #만약 display 에  _ 가 없으면 (문자가 다 체워지면)
        end_of_game = True  #while문 종료
        print("You win.")   #이겼다고 출력

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])