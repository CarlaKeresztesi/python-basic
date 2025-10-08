#   Functions - a block of code that we can reuse, that performs an operation, as many times as needed,
#   without the need for a class.
# Method - belongs to a class and only available to use when that class is instantiated.

# DRY code = Dont Repeat Yourself

def print_hello_world() :
    print("Hello World!")
    # here we have created the function and below we are calling it, otherwise it will not print anything:
print_hello_world()

# Function parameters - allow something to be passed to the function:
def double_plus_one(number):
    result = number * 2 + 1
    print(result)
double_plus_one(9)

# Multiple parameters:
def print_name(first_name, last_name):
    print(first_name + ' ' + last_name)
print_name('Mary', 'Poppins')

# The 'return' statement - functions (and methods) should change or return something:
def double_plus_one(number):
    result = number * 2 + 1
    return result
x = double_plus_one(5)
print(x)

