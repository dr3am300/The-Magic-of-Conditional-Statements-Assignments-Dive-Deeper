# Objective:
# Harness the power of conditional statements to compare and determine values.
# Task 1: Identify the Greatest------------------------------------------
# Write a Python program that prompts the user to enter three numbers. The program should then identify and print out the largest number among the three.

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
if number1 > number2 and number1 > number3:
    print("The greatest number is", number1)
elif number2 > number1 and number2 > number3:
    print("The greatest number is", number2)
else:
    print("The greatest number is", number3)

# Task 2: Identify the Smallest---------------------------------------------
#Extend your program from Task 1 to also determine the smallest number among the three and print it out.

number1 = int(input("Enter the first number: "))    
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
if number1 < number2 and number1 < number3:
    print("The smallest number is", number1)
elif number2 < number1 and number2 < number3:
    print("The smallest number is", number2)
else:
    print("The smallest number is", number3)

# Task 3: Equality Check---------------------------------------------------
# Enhance your program to handle cases where two or all of the numbers are equal. 
# The program should display appropriate messages like "Two numbers are equal and the largest" or "All numbers are equal".
# Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that "The smallest number is 3. 
# The largest number is 4. There are two numbers equal to each other." 
# Printing out which numbers are equal would be a great added bonus.

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

if number1 == number2 == number3 or number1 == number2 or number1 == number3 or number2 == number3:
    print("All numbers are equal.")
elif number1 > number2 or number1 > number3:
    print("The greatest number is", number1)
elif number2 > number1 or number2 > number3:
    print("The greatest number is", number2)
else:
    print("The greatest number is", number3)



