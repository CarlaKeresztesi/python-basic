""""" Control flow = the order in which 
           - individual statements, 
           - instructions or 
           - function calls 
    are executed or evaluated.
    
https://www.pythoncheatsheet.org/cheatsheet/control-flow 

    If statements:
        --> evaluate an expression, and if that expression is True, it then executes the following indented code.
        (will take a parameter (data), compare against a set rule and split processes based on the criteria defined.)
        
    Else statement:
        --> executes only if the evaluation of the 'if' and all the 'elif' expressions are False:

    Elif statement:
        --> executes only if the 'if' expression is False:
        
        
    Ternary Conditional Operator -> <expression1> if <condition> else <expression2>  
        --> it offers one-line code to evaluate the first expression if the condition is true, 
        and otherwise it evaluates the second expression.  
        
"""""

"""""
if example:
"""""
if 2 == 2:
    print("These numbers are equal.")

"""""
if-else example:
"""""
payment = 19
if payment > 20 :
    print("notification sent")
else:
    print('payment continues')

""""" 
if-elif example:
"""""
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

""""" Logical operators:
   and - returns true if both statements are true
   or - returns true if one of the statements is true
   not - reverses the result, if True returns False
"""""
payment = 52
if payment > 20 and payment <= 50:
    print("notification sent")
elif payment > 50:
    print("manual check")
else: print("payment continues")
