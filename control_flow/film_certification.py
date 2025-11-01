"""""
Exercise 1 - write an age checker for a cinema:

Rules:
1. if someone is under 12 - U, PG and 12 films are available
2. if someone is under 15 - U, PG and 12, 15 films are available
3. if someone is over 18 - all films are available

"""""

customer_age = 12

if customer_age <= 12:
    print("U, PG and 12 films are available")
elif customer_age <= 15:
    print("U, PG and 12, 15 films are available")
else: print("all films are available")

"""""
Exercise 2 - update cinema age checker to reflect below:
# If a customer is less than 12 - return "parental guidance"
# If a customer is between 12-14 - return "U, PG and 12 films are available"
# If a customer is between 15-17 - return "U, PG and 12, 15 films are available"
# If a customer is 18 or above - return "all films are available"
"""""
customer_age = 5

if customer_age < 12 :
    print("parental guidance")
elif customer_age >= 12 and customer_age < 15 :
    print("U, PG and 12 films are available")
elif customer_age >= 15 and customer_age < 18 :
    print("U, PG and 12, 15 films are available")
else: print("all films are available")

"""""
    --> Note that there is a more efficient solution to be found based on remembering that each condition is checked
separately top-to-bottom. Can you find it?
"""""

customer_age = 12

if customer_age < 12 :
    print("parental guidance")
elif customer_age < 15 :
    print("U, PG and 12 films are available")
elif customer_age < 18 :
    print("U, PG and 12, 15 films are available")
else:
    print("all films are available")