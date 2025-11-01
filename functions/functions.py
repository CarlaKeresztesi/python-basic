""""" 
    FUNCTION = a block of code that we can reuse, that performs an operation, 
                as many times as needed, without the need for a class.
                
    METHOD -> belongs to a class and only available to use when that class is instantiated.

    DRY code = Dont Repeat Yourself - functions make the code organised and reusable!
    
        'def functionName(value): 
            return or another action'
"""""

def print_hello_world() :
    print("Hello World!") # here we have created the function and below we are calling it, otherwise it will not print anything:
print_hello_world()

"""""
    Function parameters - allow something to be passed to the function:
    * if a function requests an argument, we must provide it with data for that argument, otherwise -> error
"""""
def double_plus_one(number):
    result = number * 2 + 1
    print(result)
double_plus_one(9) # 9 is the data for the argument

""""" 
    Multiple parameters:
"""""
def print_name(first_name, last_name):
    print(first_name + ' ' + last_name)
print_name('Mary', 'Poppins')   # 'Mary' and 'Poppins' are the data for the argument

"""""
    The 'return' statement - we use functions (and methods) to return something 
                - either to merely be used by another function
                - or used in another part of the program.
"""""
# Example 1:
def full_name(first_name, last_name):  # --> inner function
    return first_name + ' ' + last_name    # this only returns a string, it doesn't action it
# print(full_name('James', 'Lucy'))        # can print here or create a new function for printing the result.
def print_name(data_type):             # --> outer function
    print(data_type)                       # data_type is a parameter name - whatever the inner function full_name() returns
print_name(full_name('James', 'Lucy'))    # becomes the argument passed to the outer function print_name()

#Example 2:
def double_plus_one(number):
    result = number * 2 + 1
    return result
x = double_plus_one(5)
print(x)

