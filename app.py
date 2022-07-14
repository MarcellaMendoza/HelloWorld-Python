# DECLARING VARIABLES
# age = 26
# price = 19.95
# first_name = "Marcella"
# is_online = False
# print(age)

# STRING CONCATENATION
# name = input("What is your name? ")
# print("Hello " + name)

# INT FUNCTION
# birth_year = input("Enter your birth year: ")
# age = 2022 - int(birth_year)
# print(age)

# int() - turns a variable into an integer
# float() - turns a variable into a decimal
# bool() - turns a variable into a boolean (true or false value)
# str() - turns a variable into a string

# INPUT, FLOAT, AND CONCATENATION 1
# first = input("First: ")
# second = input("Second: ")
# sum = float(first) + float(second)
# print("Sum: " + str(sum))

# INPUT, FLOAT, AND CONCATENATION 2
# first = float(input("First: "))
# second = float(input("Second: "))
# sum = first + second
# print("Sum: " + str(sum))

# STRINGS
# course = 'Python for Beginners'
# print(course.upper())
# print(course)
# print(course.lower())
# print(course.find('y')) index of y is 1
# print(course.find('for')) index of for is 7
# print(course.replace('for', '4'))
# print(('Python' in course))

# ARITHMATIC OPERATORS
# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3) division operator prints out decimal
# print(10 // 3) division operator prints out whole integer
# print(10 % 3) modulus operator prints out remainder of division
# print(10 ** 3) exponent operator 10 to the power of 3

# AUGMENTED ASSIGNMENT OPERATOR
# x = 10
# x = x + 3
# x += 3
# x -= 3
# x *= 3
# print(x)

# OPERATOR PRECEDENCE
# x = (10 + 3) * 2
# print(x)

# COMPARISON OPERATORS
# x = 3 > 2
# x = 3 < 2
# x = 3 <= 2
# x = 3 >= 2
# x = 3 == 2
# x = 3 != 2
# print(x)

# LOGICAL OPERATORS
# price = 5
# print(price > 10 and price < 30)
# print(price > 10 or price < 30)
# print(not price > 10)
#
# and (both)
# or (at least one)
# not (inverses any value given)

# IF STATEMENTS
# temperature = 14
#
# if temperature > 30:
#     print("It's a hot day!")
#     print("DRINK PLENTY OF WATER!")
# elif temperature > 20: # (20, 30)
#     print("It's a nice day!")
# elif temperature > 10:
#     print("It's a bit cold.")
# else:
#     print("It's cold!")
# print("Done")

# EXCERISE
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
     converted = weight / 0.45
     print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))

# WHILE LOOPS
# i = 1
# while i <= 10:
#     print(i * '*')
#     i = i + 1

# LISTS
# names = ["Sebastian", "Marcella", "Coco", "Cosmo"]
# print(names[1])
# print(names[-1])
# print(names[-2])
# names[0] = "Sebas"
# print(names)
# print(names[0:3]) # will return a new list and stop at index 3

# LIST METHODS
# numbers = [1, 2, 3, 4, 5]
# numbers.append(6) # adds 6 to the end of the list
# numbers.insert(0, -1) # inserts -1 at index 0
# numbers.remove(3) # removes 3 from the list
# # numbers.clear() #clears the entire list
# print(numbers)
# print(1 in numbers) #boolean
# print(10 in numbers) #prints if 10 is in numbers - boolean
# print(len(numbers)) # prints number of items in list

# FOR LOOPS
# numbers = [1, 2, 3, 4, 5]
# for item in numbers:
#     print(item)
#
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i = i + 1

# RANGE FUNCTION
# numbers = range(5, 10 ,2) # 1st value is starting value - 2nd value is ending value - 3rd value is used as a step
# for number in numbers:
#     print(number)

# for number in range(5): #don't need to store range function in a variable - can use it in the for loop
#     print(number)

# TUPLES
# numbers = (1, 2, 3, 3) #we use brackets to define a list & parentheses to define a tuple
# print(numbers.count(3)) #prints how many times 3 is shown in the tuple
# print(numbers.index(3)) #prints the index of 3