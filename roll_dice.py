import random
roll = random.randint(1, 6)
print("The dice rolled: " + str(roll))
guess = int(input("Guess the number (1-6): \n"))
if guess == roll:
    print("You guessed it right! " + str(roll))
else:
    print("Sorry, the correct number was: " + str(roll))