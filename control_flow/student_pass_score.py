""""" https://www.w3schools.com/python/ref_random_randint.asp 
Exercise:
    We want to establish whether a student has passed a course. 
    Given the code above , What condition should go in place of 'HERE'

studentScore !< passingScore
studentScore == passingScore
studentScore .gt. passingScore
--> CORRECT ANSWER: studentScore >= passingScore
studentScore < passingScore
"""""
import random

passingScore = 65
studentScore = random.randint(0,100)

if studentScore >= passingScore:
    testResult = True
else:
    testResult = False

print(testResult)