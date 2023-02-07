import random

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


player_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))

if player_option == 0:
    print(rock)

elif player_option == 1: 
    print(paper)

else: print(scissors)

computer_option = random.randint(0, 2)
print("Computer choose: ")


if computer_option == 0:
    print(rock)

elif computer_option == 1: 
    print(paper)

else: print(scissors)






if player_option == computer_option: 
    print("tie!")

elif player_option == 1 and computer_option == 0:
    print("You Win!")

elif player_option == 0  and computer_option == 2:
    print("You Win!")

elif player_option == 2 and computer_option == 1:
    print("You Win!")

else: print("You lose!")





