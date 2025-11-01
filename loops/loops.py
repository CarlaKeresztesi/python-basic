#   Loops = iterators = a program that will iterate over a sequence of items.
#    - regularly used with collections(list and dictionaries) and alongside control flow(if)
#    - in Python, we used 2 key types of loops -> while and -> for loops

# for... loops - rely on iterables(- in Python that is a list, a dictionary or a string) to know how many iterations to complete

shopping_list = ['eggs', 'milk', 'bread', 'coffee']

for grocery in shopping_list:
    print('- ' + grocery)

# Let's break this down word by word:
#
# --> for - this is the Python keyword that starts the for loop structure
# --> grocery - this tells Python that this is the name for the parameter that will represent each item
# --> in - another Python keyword that has two EXTREMELY useful attributes
# --> shopping_list - this is our list that we will iterate through
# --> : - this is the end of the for loop declaration
# --> print(grocery) - this is where we use the named parameter

# for... in with list made of numbers:
def double_numbers(num_list):
    doubled = []

    for num in num_list:
        doubled.append(num * 2)
    return doubled

numbers = [1, 2, 3, 4]
print(double_numbers(numbers))

# for... in with dict:
customers = {
    "name": "Ollie",
    "eye-colour": "brown",
    "age": 45,
    "likes-chocolate": True
}

for customer in customers.values():
    print(customer)

# while loop - loop that runs whilst a condition is true

# infinite loop example:
# while True:
#     print("Loop is running!")

counter = 0
while counter < 10:
    print(counter)
    counter += 1 # if i don't increment the counter it stays at 0 so it is still an infinite loop
