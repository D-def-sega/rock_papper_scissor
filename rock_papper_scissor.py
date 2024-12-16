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

game_image = [rock, paper, scissors]

print("Let's play rock, paper and scissors \n")
player = int(input("Choose 0 for Rock, 1 for Paper and 2 for Scissors \n"))
opponent = int(random.randint(0,2))

if player > 2 or player < 0:
    print("invalid number")
else:
    print(f"Player choose {game_image[player]}")
    print(f"Opponent choose {game_image[opponent]}")

    if player == opponent:
        print("Draw")
    elif (player == 0 and opponent == 2) or (player == 1 and opponent == 0) or (player == 2 and opponent == 1):
        print("You Win")
    else:
        print("You Lose")

