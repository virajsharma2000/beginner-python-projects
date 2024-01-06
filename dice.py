#!/usr/bin/python3
import random

def roll():
    min_value = 1
    max_value = 6

    roll = random.randint(min_value, max_value)
    
    return roll


while True:
 key = input('Enter C to continue, E to exit: ')

 if key.capitalize() == 'C':
  value = roll()

  print(value)

 elif key.capitalize() == 'E':
  print('thank you for playing')
  break

 else:
  print('Unknown letter')
