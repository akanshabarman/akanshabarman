import random

def game(comp, b):
    if comp==b:
        return None
    elif comp== 'r':
        if b=='s':
            return 0
        elif b=='p':
            return 1
    elif comp== 'p':
        if b=='s':
            return 1
        elif b=='r':
            return 0
    elif comp== 's':
        if b=='p':
            return 0
        elif b=='r':
            return 1

randNo = random.randint(1,3)

if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

b= input("Player's Turn: Rock(r), Paper(p) or scissor(s) ?")

a=game(comp,b)
if a== None:
    print("Draw!")
elif a:
    print("You win")
else:
    print("You lose")

print(comp)