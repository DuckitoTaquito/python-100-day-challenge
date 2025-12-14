while True:
    print("""
    ------------------------------------------------
    Welcome to Duckito's mad lib generator! 🦆
    ------------------------------------------------
    """)

    print("""
    ------------------------------------------------
    Select one of the options below.
    1) The Awkward Superhero
    2) The Terrible Restaurant
    3) College Disaster Day
    4) The Bad Wizard Spell
    5) The Worst Pet Ever
    6) The Suspicious Job Interview
    7) The Gym Experience
    8) The Time Travel Accident
    9) The Group Project
    10) The Embarrassing Moment
    ------------------------------------------------
    """)

    option = int(input("Enter a number 1-10"))

    if option == 1:
        print("You chose: The Awkward Superhero")
        name = input("Enter a name: ")
        adjective = input("Enter an adjective: ")
        noun = input("Enter a noun: ")
        place = input("Enter a place: ")
        verb = input("Enter a verb ending in ing: ")
        print(f"{name} was the most {adjective} superhero in {place}. Instead of fighting crime, they carried a giant {noun} and spent most of their time {verb} in public. Crime rates dropped anyway—mostly from embarrassment.")
    elif option == 2:
        print("You chose: The Terrible Resturant")
        adjective = input("Enter an adjective: ")
        food = input("Enter a type of food: ")
        number = input("Enter a number: ")
        verb = input("Enter a past tense verb: ")
        animal = input("Enter an animal: ")
        print(f"I went to a {adjective} restaurant and ordered {food}. After waiting {number} minutes, the waiter {verb} and dropped my food on a {animal}. Five stars. Would not recommend.")
    elif option == 3:
        print("You chose: College Disaster Day")
        name = input("Enter a name: ")
        adjective = input("Enter an adjective: ")
        clothing_item = input("Enter a piece of clothing: ")
        verb = input("Enter a past tense verb: ")
        place = input("Enter a place: ")
        print(f"{name} woke up late wearing a {adjective} {clothing_item}. They {verb} all the way to {place} only to realize it was Sunday.")
    elif option == 4:
        print("You chose: The Bad Wizard Spell")
        wizard_name = input("Enter a wizard's name: ")
        adjective = input("Enter an adjective: ")
        spell_name = input("Enter a spell name: ")
        noun = input("Enter a noun: ")
        sound_effect = input("Enter a sound effect: ")
        print(f"Wizard {wizard_name} attempted a {adjective} spell called {spell_name}. Instead of magic, a {noun} appeared and made a loud \"{sound_effect}\". The wizard was banned immediately.")
    elif option == 5:
        print("You chose: The Worst Pet Ever")
        animal = input("Enter an animal: ")
        adjective = input("Enter an adjective: ")
        verb = input("Enter a verb: ")
        place = input("Enter a place: ")
        object = input("Enter an object: ")
        print(f"My pet {animal} is extremely {adjective}.\nEvery day it {verb} around the {place}\nand steals my {object}.\nI still love it, unfortunately.")
    elif option == 6:
        print("You chose: The Suspicious Job Interview")
        job_title = input("Enter a job title: ")
        adjective = input("Enter an adjective: ")
        verb = input("Enter a verb ending in ing: ")
        noun = input("Enter a noun: ")
        number = input("Enter a number: ")
        print(f"I interviewed for a {job_title} position.The interviewer was very {adjective}\nand kept {verb} a {noun}.\nAfter {number} minutes, I was hired.")
    elif option == 7:
        print("You chose: The Gym Experience")
        adjective = input("Enter an adjective: ")
        body_part = input("Enter a body part: ")
        verb = input("Enter a past tense verb: ")
        number = input("Enter a number: ")
        food = input("Enter a type of food: ")
        print(f"I went to the gym feeling {adjective}.After working out my {body_part},\nI {verb} for {number} seconds\nand rewarded myself with {food}.")
    elif option == 8:
        print("You chose: The Time Travel Accident")
        year = input("Enter a year: ")
        adjective = input("Enter an adjective: ")
        verb = input("Enter a past tense verb: ")
        noun = input("Enter a noun: ")
        celebrity = input("Enter a celebrity's name: ")
        print(f"I traveled back to the year {year}. Everything was {adjective}. I accidentally {verb} a {noun} and met {celebrity}. Time travel is banned now.")
    elif option == 9:
        print("You chose: The Group Project")
        adjective = input("Enter an adjective: ")
        number = input("Enter a number: ")
        verb = input("Enter a past tense verb: ")
        excuse = input("Enter an excuse: ")
        emotion = input("Enter an emotion: ")
        print(f"Our group project was {adjective}. Only {number} people showed up. One person {verb} and said \"{excuse}\". I felt extremely {emotion}.")
    elif option == 10:
        print("You chose: The Embarrassing Moment")
        place = input("Enter a place: ")
        adjective = input("Enter an adjective: ")
        verb = input("Enter a past tense verb: ")
        clothing_item = input("Enter a piece of clothing: ")
        sound_effect = input("Enter a sound effect: ")
        print(f"At {place}, I did something {adjective}. I {verb} while wearing a {clothing_item} and everyone heard \"{sound_effect}\".I have never returned.")
    else:
        print("Invalid option selected. defaulting to The Awkward Superhero.")
        name = input("Enter a name: ")
        adjective = input("Enter an adjective: ")
        noun = input("Enter a noun: ")
        place = input("Enter a place: ")
        verb = input("Enter a verb ending in ing: ")
        print(f"{name} was the most {adjective} superhero in {place}. Instead of fighting crime, they carried a giant {noun} and spent most of their time {verb} in public. Crime rates dropped anyway—mostly from embarrassment.")

    again = input("Would you like to play again? (y/n): ").strip().lower()
    if again != "y":
        print("\nThank you for using Duckito's mad lib generator! 🦆")
        break