r = 7
z = 1
from random import*
y = randint(0,20)
print('Anleitung: \nFinde die ganze Zahl zwischen 0 und 20.')
while z == 1:
      r = float(input('\nDeine Zahl:'))
      if r < y:
            print('zu niedrig! nochmal!!!')
      if r > y:
            print('zu hoch! nochmal!!!')
      if r == y:
            print('Herzlichen Glückwunsch! die zahl war ',y,'!')
            y = randint(0,20)
