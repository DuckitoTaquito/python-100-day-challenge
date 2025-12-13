#While true loops around all of this until the user doesnt want to roll dice anymore
while True:
#Import random to use for dice later
    import random
#Asks user how many dice they want to roll and the input stores that number for later
    print("How many dice would you like to roll?")
    dice_rolled = int(input("Enter a number:"))
#Asks user how many sides they want on each die and stores that data for later
    print("How many sides on each die?")
    sides = int(input("Enter a number:"))
#Empty variables to store data into
    dice_tally = 0
    number_rolled = 0
    average_roll = 0
#This is used for the average dice total
    original_dice = dice_rolled
#The loop that rolls the dice and adds it into a total and average
    while dice_rolled > 0:
        number_rolled = random.randint(1, sides)
        print(f"You rolled a {number_rolled}")
        if number_rolled == sides:
            print("Critical hit")
        if number_rolled == 1:
            print("Critical fail")
        dice_tally += number_rolled
        dice_rolled += -1
#Uses the original dice from earlier to calculate our average
    average_roll = dice_tally / original_dice
#Shows the user what their rolls were and the average of each die
    print(f"Your total is {dice_tally}")
    print(f"Your average roll was {average_roll}")
#Asks the user if they want to continue rolling dice
    again = input("Would you like to roll again? (y/n): ").strip().lower()
    if again != "y":
        print("Goodbye!")
        break