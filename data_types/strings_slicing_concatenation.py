"""   Strings = text contained within double quotes or single quotes.
"""
print("A string is text in quotes")
print('A string is text in quotes')

""" the Escape character \
"""
print("Jane said \"Hi!\"")

""" Unicode characters - all coding languages see unicode characters within double or single quotes, not sentences or paragraphs
"""
print(u'\u0061')  # letter a

""" To access characters in a string -> use their index
"""
print("hello world"[1])  #we get 'e'
print("hello world"[-1])  # we get the last character in the string
print("hello world"[-2])  # we get the penultimate character in our string

"""String slicing -> string[start:end] 
    - start is inclusive and end is exclusive
    - both start and end are optional
        - if you omit start, it means start from index 0;
        - if you omit end, it means go all the way to the end of the string.
"""
# Exercise:
# Given that a variable, name, has been assigned the value 'Bibhutibhushan Bandyopadhyay',
# which TWO of the following statements will result in an error at runtime?
name = 'Bibhutibhushan Bandyopadhyay'
print(name[4])
print(name[15:30]) # prints starting from index 15, finishing at 30- which is out of bounds - EXCLUSIVE
print(name[15:])   # prints everything starting from index 15 inclusive - up to end of string

firstInitial = name[-2] #take the penultimate character of string name and store in firstInitial variable
print(firstInitial)

""" len or length -> built in method which gives us the length of a particular object
"""
print(len("hello world"))

""" Concatenation = joining strings together with the + operator
"""
print("Jane" + "Doe")
print("Jane" + " " + "Doe")

print("number" + " " + "4")
