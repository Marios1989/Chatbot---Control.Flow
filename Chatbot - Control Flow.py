# Boolean Expressions
#My dog is the cutest dog in the world.
example_statement = "No"
# Dogs are mammals.
statement_one = "Yes"
# My dog is named Pavel.
statement_two = "Yes"
# Dogs make the best pets.
statement_three = "No"
# Cats are female dogs.
statement_four = "Yes"

# Relational Operators: Equals and Not Equals
(5 * 2) - 1 == 8 + 1
# statement_one = True
13 - 6 != (3 * 2) + 1
# statement_two = False
3 * (2 - 1) == 4 - 1
# statement_three = True

# Boolean variables
my_baby_bool = "true"
print(type(my_baby_bool))
my_baby_bool_two = True
print(type(my_baby_bool_two))

# If statement
# Enter a user name here, make sure to make it a string
user_name = "Dave"

if user_name == "Dave":
    print("Get off my computer Dave!")

user_name = "angela_catlady_87"

if user_name == "angela_catlady_87":
    print("I know it is you, Dave! Go away!")

# Relational Operators II
x = 20
y = 20

# Write the first if statement here:
if x == y:
    print("These numbers are the same")

credits = 120

# Write the second if statement here:
if credits >= 120:
    print("You have enough credits to graduate!")

# Boolean Operators: and
statement_one = False

statement_two = True

credits = 120
gpa = 3.4

if gpa >= 2.0 and credits >= 120:
    print("You meet the requirements to graduate!")

# Boolean Operators: or
statement_one = True

statement_two = True

credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
    print("You have met at least one of the requirements.")

# Boolean Operators: not
statement_one = not (4 + 5 <= 9)

statement_two = not (8 * 2) != 20 - 4

credits = 120
gpa = 1.8

if not credits >= 120:
    print("You do not have enough credits to graduate.")
if not gpa >= 2.0:
    print("Your GPA is not high enough to graduate.")
if not (credits >= 120) and not (gpa >= 2.0):
    print("You do not meet either requirement to graduate!")

# Else statements
credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
    print("You meet the requirements to graduate!")
else:
    print("You do not meet the requirements to graduate.")

# Else If Statements
grade = 86
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

# Review
print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

weight = 185
planet = 3

# Write an if statement below:
if planet == 1:
    weight = weight * 0.91
elif planet == 2:
    weight = weight * 0.38
elif planet == 3:
    weight = weight * 2.34
elif planet == 4:
    weight = weight * 1.06
elif planet == 5:
    weight = weight * 0.92
elif planet == 6:
    weight = weight * 1.19

print("Your weight:", weight)
