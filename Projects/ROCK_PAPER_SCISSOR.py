import random

def gameWin(comp, me):
    if comp == me:
        return None

    if comp=='r':
        if me == 's':
            return False
        elif me == 'p':
            return True

    elif comp=='p':
        if me == 'r':
            return False
        elif me == 's':
            return True

    elif comp=='s':
        if me == 'r':
            return True
        elif me == 'p':
            return False


print("Computer's Turn: Rock(r), Paper(p) or Scissor(s)?")
randomNo= random.randint(1, 2)

if randomNo == 1:
    comp = 'r'
elif randomNo == 2:
    comp = 'p'
elif randomNo == 3:
    comp = 's'

me = input("Your Turn: Rock(r), Paper(p) or Scissor(s)?\n")
a= gameWin(comp, me)

print(f"computer choose {comp}")
print(f"you choose {me}")

if a == None:
    print("This game is a Tie!")
elif a:
    print("You win!")
else:
    print("You lose")
    