import random;
rock = 1
paper = 2
scissors = 3

life = 5
turn = 10
computer = 0
mine = 0

while life > 0 and turn > 0:
    print("start turn ", turn)
    mineStr = input("yours: ")
    mine = int(mineStr)
    computer = random.randint(1,3)
    print("computer: ", computer)
    if mine == rock:
        if computer == paper:
            life -= 1
        if computer == scissors:
            life += 1
    if mine == paper:
        if computer == rock:
            life += 1
        if computer == scissors:
            life -= 1
    if mine == scissors:
        if computer == rock:
            life -= 1
        if computer == paper:
            life += 1
    print("life: ", life, ", end turn ", turn)
    turn -= 1

if life == 0 and turn > 0:
    print("you lose")
elif life > 0 and turn == 0:
    print("you win")
else:
    print("draw")

