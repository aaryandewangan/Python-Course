import random

def game(comp, user):
    if comp == user:
        return 0
    elif (comp == 1 and user == 2):
        return -1
    elif (comp == 2 and user == 3):
        return -1
    elif (comp == 3 and user == 1):
        return -1
    else:
        return 1


hand = int(input("What you are going to do - \n 1. Snake \n 2. Water \n 3. Gun \n Choice: "))
comp = random.randint(1, 3)

print(f"Your Hand: {hand}")
print(f"Computer's Hand: {comp}")

score = game(comp, hand)
if(score == 0):
    print("Its a Draw !")
elif(score == -1):
    print("You Lose !")
else:
    print("You win !")