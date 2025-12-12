print("""
      --------------------------
      1: Hello, World!
      2: Hello (your name)!
      3: Friendly message
      4: All uppercase
      5: All lowercase
      6: Reversed
      7: Repeated
      8: Banner style
      9: Emoji style
      """)


variations = int(input("What style of hello world would you like? (1-9): "))




if variations == 1:
    print("Hello, World!")
elif variations == 2:
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
elif variations == 3:
    print("Hey there! Hope you're having a great day!")
elif variations == 4:
    print("HELLO, WORLD!")
elif variations == 5:
    print("hello world!")
elif variations == 6:
    print("!dlroW ,olleH")
elif variations == 7:
    print("Hello World! " * 3)
elif variations == 8:
    name = input("Enter your name: ")
    print("+----------------------+")
    print(f"Hello {name}!")
    print("+----------------------+")
elif variations == 9:
    print("Hello World 🌐")
else:
    print("Incorrect input choose between 1-9 please")