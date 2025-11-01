#   Exercise combining function, loops and control flow:

#    We take a two-dimensional array:
#   two_dimensional_array = [[2, 4, 5], [1, 6, 9], [4, 7, 4]]
#   2 4 5
#   1 6 9
#   4 7 4
#   Create a function that would iterate through each list to check if a value was present within a sublist.
#   For example, let's count the 4s:

def four_counter(two_d_list): #def four_counter(two_d_list): the name of a function that expects a parameter of a two-dimensional list
    four_count = 0            #variable that will be our 'counter' and will be incremented dependent on an if statement check
    for list_item in two_d_list: #for loop with a parameter of list_item, which we will use to evaluate each embedded list in our two_d_list
        for number in list_item: #for loops through the numbers of list_item
            if number == 4:      #condition if that number is 4
                four_count += 1  #then we increment the counter
    return four_count

two_dimensional_list = [[2, 4, 5], [1, 6, 9], [4, 7, 4]]

print(four_counter(two_dimensional_list))
