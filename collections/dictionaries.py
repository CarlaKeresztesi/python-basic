""""" COLLECTIONS:
For storing larger sets of data, Python has Collections.

    Dictionaries = dicts (hashMaps or maps in other languages)
        --> key:value pairs --> we reference the key to access the value.
        
        --> Access: through the key we get the value
        
        --> dictionaries keys are often string values;
        
        --> dictionaries values can be any data type => strings, numbers, booleans, lists or even embedded dictionaries.
        
        https://docs.python.org/3/library/stdtypes.html#mapping-types-dict 
"""""

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car)

"""""
 A list is a collection of similar items ["ford", "mercedes", "mazda"]
 A dictionary provides more detail about a particular object: i.e. car - brand, model, year, engine size, colour, etc.
"""""

print(car.get('brand'))
print(car.get('model'))
print(car.get('year'))

""""" 
Python 3.7 onwards the dictionaries are ordered -> they retain their order.
Python 3.6 and before dictionaries do not retain their order
"""""

stock = {
   't-shirts' : 10,
   "dresses" : 15,
   "boots" : 8
}
print(stock)

"""""
 Working with Dictionaries:

    keys() method:
"""""

stock = {
  't-shirts' : 10,
  'dresses' : 15,
  'boots' : 8
}
print(stock.keys())

""""" 
    values() method:
"""""
print(stock.values())

""""" 
    access a specific value -> get() method:
"""""
print(stock.get("dresses"))

"""""
    use [] to access items from a dict, similar to using index in a list:
 """""
print(stock["t-shirts"])

"""""
    adding an item to a dict:
"""""
stock["hats"] = 12
print(stock)

"""""
    update() method - to change multiple items in the dict
"""""
stock.update({"hats": 10, "socks":2})
print(stock)

"""""
    pop() method to remove an item from a dict:
"""""
stock.pop("dresses")
print(stock)

