"""demo for string formatting"""

import math


def compute(radius):
    """function definition"""
    return math.pi * radius ** 2


try:
    user_radius = float(input('enter the radius: '))
    area = compute(user_radius)  # calling a function
    print('given radius: {} \narea: {:.3f}'.format(user_radius, area))

except ValueError as error:
    print(error)
