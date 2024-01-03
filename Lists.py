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


#Here is one example of using a while loop to select the user inputed values out of a list to create a word that is three letters long:
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
 "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
  "T", "U", "V", "W", "X", "Y", "Z"]

#your code goes here
counter = 1
while counter < 4:
  print(alpha[int(input())], end='')
  counter += 1


#here is a simpler way of doing the same thing without a loop:

alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
         "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
         "T", "U", "V", "W", "X", "Y", "Z"]

# Get three numbers as input and concatenate the corresponding letters
word = alpha[int(input())] + alpha[int(input())] + alpha[int(input())]

# Print the concatenated word
print(word)

# Here are some examples of using List operations:
#Reassigning a value in a list by accessing its index:
nums = [5, 8, 2]
nums[1] = 42

print(nums)

#Lists can be added together like strings can be:

nums = [1, 2, 3]
print(nums + [4, 5, 6])

#more math with lists:

x = [2, 4]

x += [6, 8]

print(x[2]//x[0])

#Lists can be multiplied by an integer:

nums = [1, 2, 3]
print(nums * 3) 

#To check if a particular item is in a list, we can use the in operator, which will return True if it is in the list, and False if it is not in the list:

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

#The in operator is also used to determine whether or not a string is a substring of another string:
x = "hello world"

if "world" in x:
  print("Yes")

#Similarly, to check if an item is not in a list, you can use the not operator in one of the following ways:
nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

#Here is an example of using the in operator:

x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]

num = int(input())

constraint = False
while constraint == False:
    if num in x:
        print("bingo") #You can also just do this by simply using the if statement without the constraint or the while loop.  I used the while loop to give the user another chance.
        constraint = True
    else:
        num = int(input())

#Another Example:
        supported = ["Lights off", "Lock the door", 
    "Open the door", "Make coffee", "Shut down"]

#your code goes here
command = input()

if command in supported:
    print("OK")
else:
    print("Unknown")

#The for loop for lists in Python is the same as the foreach loop in C# for lists and arrays:
    
words = ["hello", "world", "spam", "eggs"]
for word in words:
  print(word + "!")

  #the for loop can be used to iterate over strings:
str = "testing for loops"
count = 0

for x in str:
  if x == 't':
    count += 1

print(count)

#Similar to while loops, the break and continue statements can be used in for loops, to stop the loop or jump to the next iteration:

text = "some text"
for x in text:
  if x == 'e':
    break
  print(x)

'''
So we’ve got the for and while loops, which can be used to execute a block of code multiple times. So which do we use and when?

Usually we’d use the for loop when the number of iterations is fixed. For example, iterating over a fixed list of items in a shopping list.

The while loop is useful in cases when the number of iterations isn’t known and depends on some calculations and conditions in the code block of the loop. For example, ending the loop when the user enters a specific input in a calculator program.

While both for and while loops can be used to achieve the same results, the for loop has a cleaner and shorter syntax, making it a better choice in most cases.
'''
#Here is one way of finding the sum of a list:

x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
sumup = 0

for e in x:
    sumup += e
print(sumup)

#And, here is another way:
x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
sumup = sum(x)
print(sumup)

#Here is an example of using the in operator inside of a for loop to determine if an inputted letter was found inside of a word in the list, and then printing each word that has that letter in it:

words = ["cat", "car", "code", "home", "learn", 
    "fun", "job", "love", "friend", "zoo", "enjoy",
    "happiness", "family", "goal", "desire"]

#your code goes here
letter = input()

for letta in words:
    if letter in letta:
        print(letta)

 #Here is another way of doing this using a list comprehension:

words = ["cat", "car", "code", "home", "learn",
         "fun", "job", "love", "friend", "zoo", "enjoy",
         "happiness", "family", "goal", "desire"]

letter = input("Enter a letter: ")

found_words = [letta for letta in words if letter in letta]
print(*found_words, sep='\n')       
