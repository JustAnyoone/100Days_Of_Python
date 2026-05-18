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

import random
Game_Images = [rock,paper,scissors]
(print

('''
-----------------------------------------------
Welcome to the Rock Paper and Scissors game
------------------------------------------------
'''))

#Player_Play -------------------------------------
Player_Choice = int(input("What do you choose ? Type 0 = Rock, 1 = Paper or 2 = Scissors :"))
if Player_Choice >= 0 and Player_Choice <= 2 :
    print(Game_Images[Player_Choice])
Computer_Choice = random.randint(0, 2)
print("Computer Choice =")
print(Game_Images[Computer_Choice])

# #Who Win ---------------------------

if Player_Choice < 0 or Player_Choice >= 3 :
    print("Invalid Number")
elif Player_Choice == 0 and Computer_Choice == 2 :
    print("You win!")
elif Computer_Choice == 0 and Player_Choice == 2 :
    print("You lose!")
elif Computer_Choice == Player_Choice :
    print("It's a draw")
elif Computer_Choice > Player_Choice :
    print("You lose!")
elif Player_Choice > Computer_Choice :
    print("You Win!")