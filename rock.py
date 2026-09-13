import random
computer_choice = random.choice(['rock', 'paper', 'scissors'])
player_choice = input("Enter your choice (rock, paper, or scissors): ")
print("Computer chose: " + computer_choice)
if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == 'rock' and computer_choice == 'scissors'):
    print("You win!")
elif (player_choice == 'paper' and computer_choice == 'rock'):
    print("You win!")
elif (player_choice == 'scissors' and computer_choice == 'paper'):
    print("You win!")
else:
    print("Computer wins!")