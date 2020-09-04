"""demo for the script """
'''demo for python script'''
# pep8 - It is the python coding standreds
try:
    name = input('enter the name:')
    city = input('enter the city:')
    zip_code = int(input('enter the postal code:'))
    # type of zip_code changed from string to int

    print('name:', name)
    print('city:', city)
    print('zip code:', zip_code)
    print(type(zip_code))
    # print('name:',name, 'city:', city)
except ValueError as error:
    print(error)

print('the next statement after try except block')
