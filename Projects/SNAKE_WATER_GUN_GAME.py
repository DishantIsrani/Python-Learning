import random

def gameWin(comp, me):
    if comp == me:
        return None

    if comp=='s':
        if me == 'w':
            return False
        elif me == 'g':
            return True

    elif comp=='w':
        if me == 'g':
            return False
        elif me == 's':
            return True

    elif comp=='g':
        if me == 'w':
            return True
        elif me == 's':
            return False


print("Computer's Turn: Snake(s), Water(w) or Gun(g)?")
randomNo= random.randint(1, 2)

if randomNo == 1:
    comp = 's'
elif randomNo == 2:
    comp = 'w'
elif randomNo == 3:
    comp = 'g'

me = input("Your Turn: Snake(s), Water(w) or Gun(g)?\n")
a= gameWin(comp, me)

print(f"computer choose {randomNo}")
print(f"you choose {me}")

if a == None:
    print("This game is a Tie!")
elif a:
    print("You win!")
else:
    print("You lose")