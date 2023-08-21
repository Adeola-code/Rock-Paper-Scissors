import random
#CHARACTERS FOR ROCK, PAPER AND SCISSORS
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
#ASK USER FOR INPUT
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#USER LOSES IF HIS INPUT IS NOT 0, 1 OR 2
if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!")
else:
  print(game_images[user_choice])
#DISPLAY THE COMPUTER'S CHOICE
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

#GAME LOGIC
if user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

