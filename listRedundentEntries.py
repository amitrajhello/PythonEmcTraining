# eliminates duplicate entries

duplicates = [2.2, 3.3, 5.3, 2.2, 3.3, 5.3, 2.2, 3.3, 5.3]

print(set(duplicates))  # list type casted to set

uniq = list(set(duplicates))  # set type casted to list
print(uniq)

