"""""
Python string methods ---> built-in methods that we can use to change or adapt areas of a string

-> str.capitalize() --> Return a copy of the string with its first character capitalized and the rest lowercased.

-> str.count(sub[, start[, end]]) --> Return the number of non-overlapping occurrences of substring sub in the range [start, end]. 
Optional arguments start and end are interpreted as in slice notation.

-> str.encode(encoding='utf-8', errors='strict') --> Return the string encoded to bytes.

-> str.endswith(suffix[, start[, end]]) --> Return True if the string ends with the specified suffix, otherwise return False. 
suffix can also be a tuple of suffixes to look for. 

--> https://docs.python.org/3/library/stdtypes.html#string-methods
"""""

first_name= 'John'
print(first_name.upper())
print(first_name.lower())
print(first_name.replace('o', '2'))