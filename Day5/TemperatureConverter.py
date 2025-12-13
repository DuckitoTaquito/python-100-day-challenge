print("""
1) Celsius --> Fahrenheit
2) Fahrenheit --> Celsius
3) Celsius --> Kelvin
4) Kelvin --> Celsius
5) Fahrenheit -- > Kelvin
6) Kelvin --> Fahrenheit
""")

conversion_type = int(input("Pick one of the options above (1-6)"))

if conversion_type == 1:
    celsius = float(input("Enter Celsius:"))
    celsius_to_fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} C = {celsius_to_fahrenheit:.2}F")
elif conversion_type == 2:
    fahrenheit = float(input("Enter Fahrenheit:"))
    fahrenheit_to_celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} F = {fahrenheit_to_celsius:.2}C")
elif conversion_type == 3:
    celsius = float(input("Enter Celsius:"))
    celsius_to_kelvin = celsius + 273.15
    print(f"{celsius} C = {celsius_to_kelvin:.2}K")
elif conversion_type == 4:
    kelvin = float(input("Enter Kelvin:"))
    kelvin_to_celsius = kelvin - 273.15
    print(f"{kelvin} K ={kelvin_to_celsius:.2}C")
elif conversion_type == 5:
    fahrenheit = float(input("Enter Fahrenheit:"))
    fahrenheit_to_kelvin = (fahrenheit - 32) * 5/9 + 273.15
    print(f"{fahrenheit} F = {fahrenheit_to_kelvin:.2}K")
elif conversion_type == 6:
    kelvin = float(input("Enter Kelvin:"))
    kelvin_to_fahrenheit = (kelvin - 273.15) * 9/5 + 32
    print(f"{kelvin} K = {kelvin_to_fahrenheit:.2f}F")
else:
    print("Error wrong input choose one of the following options")