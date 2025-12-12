#loops the calculator until the user no longer wants to use it
while True:
#Prints out a menu
      print("""
      What would you like to do today?
      1. Add
      2. Subtract
      3. Multiply
      4. Divide
      """)
#Stores the selection of the user
      selection = int(input("Pick one of the following options from the menu:"))
#Stores the number choices of the user
      num1 = float(input("What is your first number:"))
      num2 = float(input("What is your second number:"))
#Empty variable to use to calculate for later
      result = 0
#Figures out what choice the user made and then prints out the calculation
      if selection == 1:
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
      elif selection == 2:
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
      elif selection == 3:
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
      elif selection == 4:
            if num2 == 0:
                  print("Error unable to divide by zero")
            else:
                  result = num1 / num2
                  print(f"{num1} / {num2} = {result}")
#Asks the user if they want to continue if n then program closes out
      else:
            print("Error please choose one of the following options")
      again = input("Calculate again? (y/n): ")
      if again != "y" and again != "Y":
            print("Goodbye!")
            break