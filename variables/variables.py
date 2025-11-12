""""" 
    Variables are namespaces in which we can hold pieces of data.
"""""
name = "Carla" # here stored in a string -> able to store lists, dictionaries, numbers, booleans, etc.
print(name)

"""""
 The "=" sign is an assignment operator in coding, not to be confused with its mathematical usage.
"""""
x = 8
y = "bob"
z = 4.5
print(x)
print(y)
print(z)

"""""
 The "+" operator works with any type of number and with two strings, for concatenation
"""""
x = 4
y = 5 + x
z = y + x
print(y)
print(z)

""""" 
The "+=" increment operator (short for x = x + 2)
 +=   ->   x += 2   ->   x = x + 2
 -=   ->   x -= 4   ->   x = x - 4
 *=   ->   x *= 5   ->   x = x * 4
 /=   ->   x /= 4   ->   x = x / 4
"""""
x = 2
x += 2
print(x)

x = 5
y = x
x = 10
print(y)
