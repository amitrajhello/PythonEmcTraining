"""The player will be given 10 chances to guess a number, and when player gives a input, then he should get a feedback
that his number was lesser or greater than the random number """
import random

key = random.randint(1, 1000)

x = 1
while x <= 10:
    user_input = int(input('Give a random number to play the game: '))

    if user_input > key:
        print('your input is more than the number, please try again')
    elif user_input < key:
        print('your input is less than the number')
    elif user_input == key:
        print('Congratulations! you won!')
        break
    x += 1
