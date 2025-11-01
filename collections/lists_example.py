""""" 
    Lists - ideally - single data types https://docs.python.org/3/library/stdtypes.html#list
"""""

#example_list = [1, True, "string"]
#print(example_list)
#print(type(example_list))

#print(example_list[0])
#print(example_list[1])
#print(example_list[-1]) # [-1] will always return the last item in the list
#print(example_list[-2])
#print(example_list[-3])

shopping_list = ["eggs", "bread", "cheese"]
print(shopping_list)

"""""
The list is being re-written after it has been created to replace the item at index 1
"""""
shopping_list[1] = "bananas" # the list is being re-written after it has been created to replace the item at index 1
print(shopping_list)

"""""
Append method - to add items at the end of a list:
"""""
shopping_list.append("mushrooms")
print(shopping_list)

"""""
Pop method - to remove items from a list
    - without providing an index --> removes the last item from the list;
    - providing an index --> removes the item at a specific index within the list
"""""
shopping_list.pop()
print(shopping_list)

"""""
Index method - searches for a specific item in a list
"""""
print(shopping_list.index("bananas"))

# Exercise:
# Given the code below.
# What is the result of printing len(theList)?
theList = []
theList.append(1234)
theList.append(4567)
theList.append(99)
theList.append(5)
print(len(theList)) # return is 4 as we added 4 items to the list
print(theList) # returns: [1234, 4567, 99, 5]



