#List slices allow you to get a part of the list using two colon-separated indices. This returns a new list containing all the values between the indices.
#Just like the arguments to range, the first index provided in a slice is included in the result, but the second isn't.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])
#If the first number in a slice is omitted, it’s taken to be the start of the list.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
#If the second number is omitted, it’s taken to be the end.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[7:])

#Just like with ranges, your list slices can include a third number, representing the step, to include only alternate values in the slice. Like this:
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
print(squares[::2]) #This just increments through the list by 2 values
print(squares[2:8:3])

"""
Negative values can also be used in list slicing (as well as normal list indexing). 

Which means that when negative values are used for the first and second values in a slice (or a normal index), they count from the end of the list. Like this:

**If a negative value is used for the step, the slice will be done backwards.
"""
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

#Using [::-1] as a slice is a common and idiomatic way to reverse a list.
nums = [5, 42, 7, 1, 0]
res = nums[::-1]
print(res)

#Here is a way to print the last character of a string:
userInput = input()
storedValue = userInput[::-1]

print(storedValue[0])

#Another way is like this:
userInput = input()
lastCharacter = userInput[-1] #You can directly access the last character of a string by using negative indexing. In Python, -1 refers to the last character, -2 refers to the second last character, and so on. 

print(lastCharacter)

#This is how you can reverse a string:

text = input()

#your code goes here
reversedString = text[::-1]
print(reversedString)

#Here is another way using the reversed() method and the join() method to bring the characters back into a string:

text = input()
reversedString = ''.join(reversed(text))
print(reversedString)

#This is a tough one.  This is accessing the value at index 4 (which is 5) and using that value as the index it is now trying to reach (at index 5, we get the value 8):
list = [1, 1, 2, 3, 5, 8, 13]

print(list[list[4]])


