import random
dice2=random.randint(1,6)
print("The value of the computers dice is:", dice2)
import random
dice=random.randint(1,6)
print("The value of your dice is:", dice)
if dice>dice2:
    print("You win! Computer loses!")
if dice2>dice:
    print("You lose! Computer wins!")
if dice==dice2:
    print("Its a tie! No one wins!")
