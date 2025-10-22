#   Loops = iterators = a program that will iterate over a sequence of items.
#    - regularly used with collections(list and dictionaries) and alongside control flow(if)
#    - in Python, we used 2 key types of loops -> while and -> for loops

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

# example with List made of numbers:
def double_numbers(num_list):
    doubled = []

    for num in num_list:
        doubled.append(num * 2)
    return doubled

numbers = [1, 2, 3, 4]
print(double_numbers(numbers))