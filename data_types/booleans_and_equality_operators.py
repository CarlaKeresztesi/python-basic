""""
Equality operators

Operator |                   Meaning                    |         Example                   |
   ==    |    equal to                                  |      4 == 4 (True)                |
   !=    |     not equal to                             |      4 != 4 (False)               |                 
   >     |     Greater than                             |      3 > 4 (False)                |
   <     |     Less than                                |      3 < 4 (True)                 |
   >=    |     Greater than or equal to                 |      5 >= 5 (True)                |      
   <=    |     Less than or equal to                    |      5 <= 4 (False)               |  
   
  Equality operators can be used on different data types, as long as they are within the same object hierarchy 
(object hierarchy references descendants of objects acting as properties of an object. 
An example of this would be the object controlling a window (at the top of the hierarchy) having 
another object like the window's border acting as a property of the window).
"""""
print(4 == 4)
print(3 != 4)
print(2 < len("2"))

# Exercises with operators:
age = 20

if age >= 17:
    print("You can start to drive, with a supervisor")
# else... not able to start to drive...

# Math operators: +, - * / %
print(19 + 10.1)

# Modulo operator finds the remainder after the division of numbers:
print(13 % 3)

# Operator precedence = Parenthesis Exponentials Division Mupltiplication Addition Subtraction
print(10 * 4 / 2)


"""""
 Boolean Operators: True or False
"""""
print(type(True))

"""""
 Truthy or Falsey
        -> anything other than 0 is considered True in Python
"""""
# Numbers:
print(bool(1)) # returns True
print(bool(0)) # returns False
print(bool(-1)) # returns True
# Strings:
print(bool("world")) # returns True
print(bool("")) # returns False - empty string

# Exercise:
a = 12; b = 1.6
print( a/b )

