#a list can be created simply by declaring your variable by giving it a name, and by using square brackets and commas, assigning what is inside your list:
words = ['Hello', 'World', 32]
#to access the item in a list, you can simply say print(words[0]) or whatever index you are wanting to access

#We can do some pretty cool stuff with them in Python. For example, we can use nested lists to represent 2D grids, such as matrices.

m = [
    [1, 2, 3],
    [4, 5, 6]
    ]

#This is useful because a matrix-like structure can allow you to store data in row-column format, like in ticketing programs, that need to store the seat numbers in a matrix, with their corresponding rows and numbers.
#To access the elements of a matrix, we specify the row and the column of the item using square brackets:

print(m[1][2])

things = [
    "text", 
    0, 
        [
        1,
        2,
        8
        ], 
    4.56
        ]

print(things[2][2])
