# start the game
# ask the player to make a move (r , p , s)
# pc would select a move randomly
# pc == player -> tie
# (player == p and pc == rock) or (player == r and pc == sicissore) or (player == sicissore and pc == piper)
## user won / you won 
# any other 
##pc won /you lose

import random

user = input("what's your choice?'r' for rock,'p' for peper and 's' for scissors\n")
pc = random.choice(['r','p','s'])

print("user played: "+ user)
print("pc played: "+ pc)

if user == pc:
    print("it's a tie")
elif (user == 'p' and pc == 'r') or (user == 'r' and pc == 's') or (user == 's' and pc == 'p'):
    print("you won!")
else:
    print("you lose!")