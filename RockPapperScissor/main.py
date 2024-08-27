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

scissor = '''
           _______
       ---'   ____)____
                 ______)
              __________)
             (____)
       ---.__(___)

'''

You = int(input('''What do you want to choose? Type 0 for rock, 
   Type 1 for paper, Type 2 for scissors\n'''))

print("You chose!")

if You == 0:
  print(rock)
elif You == 1:
  print(paper)
elif You == 2:
  print(scissor)
else:
  print("You have entered an invalid number")

Computer = random.randint(0,2)

print("Computer chose!")

if Computer == 0:
  print(rock)
elif Computer == 1:
  print(paper)
elif Computer == 2:
  print(scissor)

if(You == Computer):
  print("It's a draw!")
elif((You == 0 and Computer == 1) or \
     (You == 1 and Computer == 2) or \
     (You == 2 and Computer == 0)):
  print("You lose!")
elif((You == 0 and Computer == 2) or \
     (You == 1 and Computer == 0) or \
     (You == 2 and Computer == 1)):
  print("You win!")  
