""""" 
    FOR LOOPS 
        - deterministic loops = it will loop over an object a determined number of times, checking every item in that object
        
        - will loop over collections of data
        
        - needs to be given an iterable object and will cycle through each object within the iterable 
        (i.e. through a list, a dictionary or a string) and return it for action;
        
        - iterables = they hold more than one data type - i.e. lists, dictionaries and strings too - as these hold a list of characters;
              
              for -placeholder variable- in -iterable object- :
                    do...
"""""

# Example 1 - string:
example_string = "test"
for character in example_string:   # character = placeholder variable
    print(character)

# Example 2 - list:
basket = ["eggs", "bread"]
for basket_item in basket:         # basket_item = placeholder variable
    print(basket_item)

# Example 3 - dictionary:
customers = {
    "name": "tess",
    "age": 28
}
# will print the keys
for customer in customers:        # customer = placeholder variable
    print(customer)

# will print the values
for customer in customers.values():        # customer = placeholder variable
    print(customer)