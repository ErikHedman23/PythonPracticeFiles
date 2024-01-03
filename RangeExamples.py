'''
Python makes it super easy to create number sequences using the range() function.

By default, it starts from 0, increments by 1 and stops before the specified number.

The following code generates a list containing all of the integers, up to 10.
'''
numbers = range(10)

#In order to output the range as a list, we need to explicitly convert it to a list, using the list() function:
numbers = list(range(10))
print(numbers)


#If range is called with one argument, it’ll produce an object with values from 0 to that argument. 

#If it’s called with two arguments, it’ll produce values from the first to the second:

numbers = list(range(3, 8))
print(numbers)

#There’s also a third argument you can use with range(), and it’s really useful. It’s called Step and it determines the interval of the sequence produced. Take a look:
numbers = list(range(5, 20, 2))
print(numbers)

#Want to go backward? No problem! We can also create a list of decreasing numbers, using a negative number as the third argument:
x = list(range(7, 3, -1))
print(x)
#You can use ranges in for loops, without the need to convert them into lists. It’s commonly used to repeat some code a certain number of times. Like this:

for i in range(5):
  print("hello!")

  '''
  You are creating a date picker for a website and need to output all of the years in a given period. 

Write a program that takes two integers as input and outputs the range of numbers between the two inputs as a list.

The output sequence should start with the first input number and end with the second input number, without including it.
'''
a = int(input())
b = int(input())

list_of_years = list(range(a, b)) #if you wanted to include the last year in the range, you would simply append the method like so: list(range(a, b + 1))
print(list_of_years)

"""
A group of buildings has a restaurant on every 5th floor.

In other words, a building with 12 floors has restaurants on the 5th and 10th floors. 

Task
Create a program that takes the total number of floors as input and outputs the floors that have restaurants.
"""
floors = int(input())

#your code goes here

building = list(range(5, floors, 5))

for floor in building:
    print(floor)