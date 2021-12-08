#Program 1 Lottery
import random
lotterygame = input("Would you like to play? (y/n): ")
while lotterygame == "y":
    FirstLotteryNumber = random.randint(0,9)
    SecondLotteryNumber = random.randint(0,9)
    ThirdLotteryNumber = random.randint(0,9)
    winningNumbers = FirstLotteryNumber, SecondLotteryNumber, ThirdLotteryNumber

    FirstNumberBet = int(input("Your First Number: "))
    SecondNumberBet = int(input("Your Second Number: "))
    ThirdNumberBet = int(input("Your Third Number: "))    
    yourNumbers = FirstNumberBet, SecondNumberBet, ThirdNumberBet

    if FirstNumberBet == FirstLotteryNumber and SecondNumberBet == SecondLotteryNumber and ThirdNumberBet == ThirdLotteryNumber:
        print(f"Your Numbers Are: {yourNumbers}")
        print(f"Winning Lottery Numbers Are: {winningNumbers}")
        print("Winner!!")
        lotterygame = input("Play Again? (y/n): ")
    else:
        print(f"Your Numbers Are: {yourNumbers}")
        print(f"Winning Lottery Numbers Are: {winningNumbers}")
        print("You Loss!")
        lotterygame = input("Try Again? (y/n): ")

if lotterygame == "n":
    print("See You Next Time!")


    

            
    
    






