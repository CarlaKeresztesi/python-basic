""""" 
    WHILE LOOPS - non-deterministic loops --> reliant on boolean conditions
                - a while loop will operate until a condition is true and once it is false it will stop; 
                - syntax of a while loop:
                       * 'while' - keyword
                       *  condition that is either true or false
                       *  ':' - colon 
                       *  action
        while -true condition- :
                do... (don't forget counter iteration)
"""""

#loop_control = False
# setting variable to False - doesn't run the while loop as the condition is false
# setting variable to True - runs an infinite loop as we haven't yet set a stop condition

counter = 0

while counter < 10:
    print("I am a loop") # if we don't add a counter iteration below, it is infinite again as the condition is always true
    counter += 1         # increment operator to iterate through counter, otherwise -> infinite loops
    print(counter)

# Add an if statement to print out whether a number is odd or not, as part of our counter

counter = 0

while counter < 10:
    if counter % 2 == 0:
        print(counter)
    else:
        print("odd number string")
    counter += 1

