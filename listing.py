import re

pattern = ' +'
list_of_file_size = []

for line in open('listing.dat'):
    content = re.split(pattern, line)
    # print(content[4])
    list_of_file_size.append(int(content[4]))

print(min(list_of_file_size))
print(max(list_of_file_size))
print(sum(list_of_file_size))
print(sum(list_of_file_size) / len((list_of_file_size)))

