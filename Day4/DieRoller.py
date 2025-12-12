while True:
    import random

    print("How many dice would you like to roll?")
    dice_rolled = int(input("Enter a number:"))

    print("How many sides on each die?")
    sides = int(input("Enter a number:"))

    dice_tally = 0
    number_rolled = 0
    average_roll = 0
    original_dice = dice_rolled

    while dice_rolled > 0:
        number_rolled = random.randint(1, sides)
        print(f"You rolled a {number_rolled}")
        if number_rolled == sides:
            print("Critical hit")
        if number_rolled == 1:
            print("Critical fail")
        dice_tally += number_rolled
        dice_rolled += -1

    average_roll = dice_tally / original_dice

    print(f"Your total is {dice_tally}")
    print(f"Your average roll was {average_roll}")

    again = input("Would you like to roll again? (y/n): ").strip().lower()
    if again != "y":
        print("Goodbye!")
        break