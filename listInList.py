mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

mat[1][1] = 'x'  # update
print(mat)
print()

mat[2].append(10)  # append an item in a row
print(mat)
print()

del mat[0][1]  # delete an item in a row
print(mat)
print()

for row in mat:         # nested for loop
    for col in row:
        print(col, end='\t')
    print()

mat.insert(1, [4, 5, 3])  # insert
print(mat)
print()
