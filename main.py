# app title
print("CALCULATOR APPLICATION")

# make endash symbol
en_dash = chr(8211)

# Prompt user to input first number, convert input into a float, 
# then store it in the num1 variable
num1 = float(input("What is the first number? "))

# Prompt user to input second number, convert input into a float, 
# then store it in the num2 variable
num2 = float(input("What is the second number? "))

# instruct user to select an operation
print("Select and operation: ")
# tell user 1 means they will add the numbers
print(f"1 {en_dash} Addition")
# tell user 2 means they will subtract the numbers
print(f"2 {en_dash} Subtraction")
# tell user 3 means they will multiply the numbers
print(f"3 {en_dash} Multiplication")
# tell user 4 means they will divide the numbers
print(f"4 {en_dash} Division")

# prompt user to enter their choice and store the int in the userChoice variable
userChoice = int(input("Enter your choice (1-4): "))

# if user's choice is 1
if userChoice == 1:
    # set result variable to the result of the equasion
    result = round(num1 + num2, 2)
    # tell user the result of their addition
    print(f"The result of addition is: {result}")
# if user's choice is 2
elif userChoice == 2:
    # set result variable to the result of the equasion
    result = round(num1 - num2, 2)
    # tell user the result of their subtraction
    print(f"The result of subtraction is: {result}")
elif userChoice == 3:
    # set result variable to the result of the equasion
    result = round(num1 * num2, 2)
    # tell user the result of their multiplication
    print(f"The result of multiplication is: {result}")
elif userChoice == 4:
    # set result variable to the result of the equasion
    result = round(num1 / num2, 2)
    # tell user the result of their division
    print(f"The result of division is: {result}")
# if choice is not in range
else:
    result = "Nothing"
    # tell user their choice was out of range
    print("Sorry, that choice is out of range. Have a lovely day!")
    
# present final result to user again
print(f"Here is the result: {result}")