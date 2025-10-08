#   If statements will take a parameter (data), compare against a set rule and split processes based on the criteria defined.

# Control flow:
# if-else
payment = 19
if payment > 20 :
    print("notification sent")
else:
    print('payment continues')

# if-elif
payment = 20
if payment >= 20 :
    print("Notify system:", "Payment over 20")
elif payment >= 50:
    print("Manual check to take place")

payment = 20
if payment >= 50 :
    print("Notify system:", "Payment over 20")
elif payment >= 20:
    print("Manual check to take place")

# Logical operators:
#   and - returns true if both statements are true
#   or - returns true if one of the statements is true
#   not - reverses the result, if True returns False

payment = 52
if payment > 20 and payment <= 50:
    print("notification sent")
elif payment > 50:
    print("manual check")
else: print("payment continues")

# Practice 1 - write an age checker for a cinema:
customer_age = 5
if customer_age >= 15 :
    print("Customer can see film")
else: print("Customer too young")

# Practice 2 - update cinema age checker to reflect below:
# If a customer is less than 12 - return "parental guidance"
# If a customer is between 12-14 - return "12 ratings and below"
# If a customer is between 15-17 - return "15 ratings and below"
# If a customer is 18 or above - return "any film"
customer_age = 5
if customer_age < 12 :
    print("parental guidance")
elif customer_age >= 12 and customer_age < 15 :
    print("12 ratings and below")
elif customer_age >= 15 and customer_age < 18 :
    print("15 ratings and below")
else: print("any film")
# Note that there is a more efficient solution to be found based on remembering that each condition is checked
# separately top-to-bottom.  Can you find it?
customer_age = 12
if customer_age < 12 :
    print("parental guidance")
elif customer_age < 15 :
    print("12 ratings and below")
elif customer_age < 18 :
    print("15 ratings and below")
else:
    print("any film")