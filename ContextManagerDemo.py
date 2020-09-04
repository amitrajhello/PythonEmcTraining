"""demo for the content manager"""

with open('passwd.txt') as fp:
    print(fp.closed)  # file is open, so false will be printed
    for temp in fp:     # printing the contents of the file
        print(temp, end='')

print()
print(fp.closed)    # checking for file is closed after exiting the with block
