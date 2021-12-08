# Program 2: Guess the Number
import random
answer = input("Would you like to guess the number? (y/n): ")
while answer == "y":
    randomNumber = random.randint(0,100)
    userAnswer = int(input("What is your guess? "))
    if userAnswer > randomNumber:
        print(f"Correct Number is {randomNumber}")
        print('Your Answer is Greater Than the Correct Number')
        answer = "y"
    if userAnswer < randomNumber:
        print(f"Correct Number is {randomNumber}")
        print("Your Answer is Less Than the Correct Number")
        answer = "y"
    if userAnswer == randomNumber:
        print("You Guessed the Right Answer!")
        break

    
        
    