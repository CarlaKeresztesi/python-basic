""""" 
Creating a basic calculator with 2 simple functions:
             - addition
             - subtraction.
 We need:
    * a function for addition
    * a function for subtraction
    * user input function --> that will return a string so we have to cast it to an integer
                          --> this function can actually take an argument and print it when running the program 
    * a variable to store the user input in                       
    
"""""
def add(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

choice = int(input('\nEnter 1 for addition and 2 for subtraction: '))

num1 = int(input('\n Input your first number: '))
num2 = int(input('\n Input your second number: '))

if choice == 1:
    print('\n The result is: ', num1, '+', num2, '=', add(num1, num2))
elif choice == 2:
    print('\n The result is: ', num1, '-', num2, '=', subtraction(num1, num2))
else:
    print('Invalid choice')
