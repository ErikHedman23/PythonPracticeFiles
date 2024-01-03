"""



for i in range(10):: This initiates a loop that iterates over numbers from 0 to 9 (total of 10 numbers).

if not i % 2 == 0:: This conditional statement checks if the number i is odd. The % operator gives the remainder of the division. i % 2 == 0 evaluates to True for even numbers and False for odd numbers. The not keyword reverses the condition, so not i % 2 == 0 checks for odd numbers.

print(i + 1): If the number i is odd (not divisible by 2), i + 1 is printed. Since i starts from 0, adding 1 to it results in printing odd numbers starting from 1.

Therefore, this code outputs the sequence of odd numbers from 1 to 9, each incremented by 1 within the loop's range of 0 to 9.

"""
for i in range(10):
    if not i % 2 == 0:
        print(i + 1)

        #To find the sum of a range from 1 to N (including N):
N = int(input())
sumation = sum(range(1, N + 1))
print(sumation)

#Another way to write this using a math formula is:
N = int(input())
sumation = N * (N + 1) // 2  # Using integer division to ensure an integer result
print(sumation)

