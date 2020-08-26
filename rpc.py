from random import choice
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

  global wins
  global loses
  wins, loses, = 0, 0

  while (wins + loses) != 3 or wins != 2 or loses != 2:

    yourChoice = ''

    interface(yourEmj, oppEmj)
    yourChoice = input('\n> ')

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

    if yourChoice == 'rock':
      yourEmj = rock
    elif yourChoice == 'paper':
      yourEmj = paper
    elif yourChoice == 'scissors':
      yourEmj = scissors

    if yourChoice == 'rock' and oppChoice == 'scissors' or yourChoice == 'paper' and oppChoice == 'rock' or yourChoice == 'scissors' and oppChoice == 'paper': 
      wins += 1
      print('You Win!')

    elif yourChoice == oppChoice:
      print('You Draw!')

    else:
      loses += 1
      print('You Lose')
    
    
      
  
  if wins > loses:
    interface(yourEmj, oppEmj)
    print('\nYou Won!')
    
  else:
    interface(yourEmj, oppEmj)
    print('\nYou Lost!')

def interface(yourEmj, oppEmj):
  global wins
  global loses

  print(f'Score: {wins}:{loses}')
  print(f'\n{yourEmj}  vs {oppEmj}')
  
main()


