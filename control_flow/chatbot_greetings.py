"""""
Exercise - ensure chatbot delivers the correct message dependent on the time of the day based on a 24hr time:

Greetings:
1. between 5am and 12pm - Good morning
2. between 12pm and 18pm - Good afternoon
3. between 18pm and 12am - Good evening

Use 'or' and 'and' keywords in your solution:
"""""

time = 28

if time > 5 and time < 12 :
    print("Good morning")
elif time >12 and time < 18 :
    print("Good afternoon")
else:
    print("Good evening")