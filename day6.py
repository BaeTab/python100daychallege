#day6 Exam1
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def cycle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


cycle()
cycle()
cycle()
cycle()
cycle()
cycle()


#Day6 Exam2
#Goal 지점이 나올때까지 while 문 이용 반복
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def cycle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    cycle()
    
#Day6 Exam3
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def cycle():
    
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        cycle()
    
   