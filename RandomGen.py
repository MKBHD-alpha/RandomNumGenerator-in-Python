import random

min_value = 1
max_value = 6

again = True

while again:

    print(random.randint(min_value, max_value))

    another_roll = input('Want to roll the die again? ')

    if another_roll.lower() == 'yes' or another_roll.lower() == 'y':
        continue
    else:
        break
