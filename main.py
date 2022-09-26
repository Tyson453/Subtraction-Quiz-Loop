# Tyson Whelan
#9/16/22
# Subtraction Quiz

import random, time

correct = 0
total = 0
NUMBER_OF_QUESTIONS = 5

startTime = time.time()

while total < NUMBER_OF_QUESTIONS:
    #Generate two random numbers
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    
    #Swap if needed
    if num1 < num2:
        num1, num2 = num2, num1
    
    answer = eval(input("What is " + str(num1) + " - " + str(num2) + "? "))
    
    if num1-num2 == answer:
        print("You are correct!")
        correct += 1
    
    else:
        print("Nope. You need to go back to 1st grade.")

    total += 1
    print()

endTime = time.time()
print(f"You got {correct} out of {total} correct in {round(endTime-startTime, 2)} seconds")