""""" 
    Dictionaries or dicts - are used to manage complex data sets https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
    - Key value pairs
    - use camelCase or '-' for readability
    - use commas to separate the dict items
"""""

contact_list = {
    "jane": "07865932458"
}
print(contact_list)
print(type(contact_list))

"""""
To access a value - use the specified key:
"""""
print(contact_list["jane"])

"""""
To add a new key-value pair to a dict - use the syntax below:
 - if the key does not exist in the dictionary, it will add the key-value pair to the dictionary
"""""
contact_list["bob"] = "08865932412"
print(contact_list) # returns: {'jane': '07865932458', 'bob': '08865932412'}

"""""
To amend a new key-value pair - use the syntax below:
 - this will amend the existing value
"""""
contact_list["bob"] = "new number"
print(contact_list)  # returns: {'jane': '07865932458', 'bob': 'new number'}

"""""
Useful methods on dictionaries:
    --> keys() --> returns all keys available in the dictionary
"""""
print(contact_list.keys()) # returns: dict_keys(['jane', 'bob'])

"""""
    --> values() --> returns all values available in the dictionary
"""""
print(contact_list.values()) # returns: dict_values(['07865932458', 'new number'])

"""""
    --> pop() --> removes a particular entry from the dictionary 
            - requires a key
            - returns the removed value
"""""
print(contact_list.pop("jane")) # returns: 07865932458

"""""
Example: how an alphabetical contact list could be managed with a Python dictionary:
"""""
contact_list = {
    "a": {
        "anne": "0854692433"
    },
    "b": {
        "bob": "269469872"
    },
    "c": {
        "charles": "56972365"
    },
}
"""""
- to print the 'b' contacts:
        * important to remember the return will be a dictionary
"""""
print(contact_list['b']) # returns: {'bob': '269469872'}

"""""
- to access all contacts under the key 'b':
        * use the keys() to return all 'b' contacts:
"""""
print(contact_list['b'].keys()) # returns: dict_keys(['bob'])

"""""
- to access a specific contact (get a contact number returned):
        * provide the necessary key within another set of sq brackets:
"""""
print(contact_list['b']['bob']) # returns: 269469872