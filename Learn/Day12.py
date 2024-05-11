import random

print("Welcome to the number Guessing Game!")
print("I'm thinking of a number  between 1 and 100")

Level = input("Choose a difficulty. Type 'easy' or 'hard' :")

Guess_Count = 0
number = random.randint(1, 100)
print(number)
if Level.lower() == "easy":
    Guess_Count = 10
else:
    Guess_Count = 5

while True:
    if Guess_Count == 0:
        print("Out of Guess ") 
        break
    print(f"You have {Guess_Count} atteps remaining to guess the number.")
    Guses_number = int(input("Make a guess : "))

    if Guses_number > number:
        print("Too high")
    elif Guses_number < number:
        print("Too low")

    else:
        print(f"You got it! The answer was {number}")
        play_again = input("Type 'y' to next or 'n' close program") 
        if (play_again.lower() == 'n') :
            break

    Guess_Count -= 1
    
        
