from random import choice
from time import sleep
from sys import stdout
from os import system
import emoji
system('clear')


def main():

  rpc = ['rock','paper','scissors']
  yourEmj = ''
  oppEmj = ''

  # print(emoji.demojize('Python is 👊'))
  # print(emoji.demojize('Python is 🖐'))
  # print(emoji.demojize('Python is ✌️'))

  rock = emoji.emojize(':oncoming_fist:')
  paper = emoji.emojize(':hand_with_fingers_splayed:')
  scissors = emoji.emojize(':victory_hand:')
  

  wins, loses, = 0, 0

  while (wins or loses) != 2:

    yourChoice = ''
    while yourChoice not in ['1','2','3']:

      yourChoice = input(f'''
 {yourEmj}  vs {oppEmj}

1. Rock
2. Paper
3. Scissors

> ''')
      print()
      print('-' * 20)
      print()

      oppChoice = choice(rpc)

      if oppChoice == 'rock':
        oppEmj = rock
      elif oppChoice == 'paper':
        oppEmj = paper
      elif oppChoice == 'scissors':
        oppEmj = scissors

      if yourChoice == '1':
        yourEmj = rock
      elif yourChoice == '2':
        yourEmj = paper
      elif yourChoice == '3':
        yourEmj = scissors

      if yourChoice == '1' and oppChoice == 'scissors' or yourChoice == '2' and oppChoice == 'rock' or yourChoice == '3' and oppChoice == 'paper': 
        wins += 1
        print('You Win!')

      elif rpc[int(yourChoice) - 1] == oppChoice:
        print('You Draw!')

      else:
        loses += 1
        print('You Lose')
      
  
  if wins > loses:
    print(f'''
  {yourEmj}  vs {oppEmj}

1. Rock
2. Paper
3. Scissors''')
    print('\nYou Won!')
    
  else:
    print(f'''
  {yourEmj}  vs {oppEmj}

1. Rock
2. Paper
3. Scissors''')
    print('\nYou Lost!')
  
 

main()

