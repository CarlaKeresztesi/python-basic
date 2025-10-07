# For storing larger sets of data, Python has Collections.

#   Lists are collections of similar items (like arrays):
["apples", "bread", "eggs"]
# if we want to use the lists, we attribute them to a variable:
shopping_list = ["apples", "bread", "eggs"]
print(shopping_list)

#   Lists are not data type specific - we can have an array with different data types in there - string, integer, float:
random_list = ["any word", 4, 20.8]

#   Access:
# To access a certain element from the list, we access it via the index, which starts at 0, i.e. to access
# the integer 4 in above:
print(random_list[1])
# the access to the list elements can also be through negative values, with index -1 retrieving the last element in the list
print(random_list[-1])

#   Append method:
# Append the word "milk" to above random_list and print it out:
random_list.append("milk")
print(random_list)

#   Removing items from a list: .pop or .pop(index number)
random_list.pop()
print(random_list)

random_list.pop(-2)
print(random_list)

removed_item = random_list.pop(1) # we can use the removed item to assign it to a variable and use it later if needed.
print(removed_item)
print(random_list)

