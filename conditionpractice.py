print('What is your age? If it is less than 18, you may be entitled to a hug...')
age = int(input())
if age < 18:
    print('You get a hug!')
else:
    print("Sorry, no hug for you.")



    
''' Here is another example, only this time using the elif (else if) to provide another condition to check for.
    age = 75
if age < 18: 
  print("Junior discount")
elif age >= 75: 
  print("Senior discount")
else:
  print("No discount")
print("Proceed to payment")
Here is a nested if statement:

age = 16
is_student = True

if age < 18:
  #execute if age is less than 18
  if is_student:
    #execute if under 18 and also a student
    print("20% discount")
  else:
    #execute if under 18 and not a student
    print("10% discount")
else:
  #execute this code customer 18 or over
  print("Regular price")

'''