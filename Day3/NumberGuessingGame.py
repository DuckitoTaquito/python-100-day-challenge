#importing random to use later for randint for my number to guess
import random
#this is the guessing game its self the while true will ask the user if they want to continue
while True:
#this print statement will ask the user to choose their difficulty
    print("""
    Choose difficulty: (1) Easy (2) Normal (3) Hard
        """)
#this input will store our difficulty selection
    difficulty = int(input("type the number to choose your difficulty"))
#number to guess to put into our difficulty selector and to use as our number to guess
    number_to_guess = 0
#difficulty selection checks what we stored earlier and if it == to the number that was prompted it chooses that difficulty otherwise it defaults to medium
    if difficulty == 1:
        number_to_guess = random.randint(1, 50)
        print("You have chosen easy. Good luck!")
    elif difficulty == 2:
        number_to_guess = random.randint(1, 100)
        print("You have chosen medium. Good luck!")
    elif difficulty == 3:
        number_to_guess = random.randint(1, 500)
        print("You have chosen Hard. Good luck!")
    else:
        number_to_guess = random.randint(1, 100)
        print("Invalid difficulty chosen: playing on medium difficulty. Good Luck!")
#this takes the users guess and stores it into the guess variable
    guess = int(input("What is your guess?"))
#this tracks the users guess attempts
    guess_tally = 1
#this loop will see if our guess isnt the number to guess if not it will add to guess_tally and print Guess #(guess attempt) while telling the user if they are too high or low if the number is right it will break the loop
    while guess != number_to_guess:
        if guess > number_to_guess:
            guess_tally += 1
            print(f"Guess #{guess_tally}")
            print("Too High!")
        elif guess < number_to_guess:
            guess_tally += 1
            print(f"Guess #{guess_tally}")
            print("Too Low")

        guess = int(input("Try again:"))
#if the number is correct and the previous loop was broken we will tell the user their guesses and the correct number
    print(f"Correct the number was {number_to_guess} You had {guess_tally} guesses")
#this checks to see if the user would like to play again if not program closes
    again = input("Would you like to play again?")
    if again != "y" and again != "Y":
            print("Goodbye!")
            break
    