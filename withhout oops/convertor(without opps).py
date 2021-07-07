# The programme which convert weight from kilos to lbs an visa versa

weight = float(input("Enter your weight: "))
unit = input("Enter the unit: ")

if unit.upper() == "L":
    converted = weight * 0.453592
    print(f"your weight is {converted} kilos")
elif unit.upper() == "K":
    converted = weight / 0.453592
    print(f"your weight is {converted}")
else:
    print("sorry!! wrong unit")
    print("please select the right unit")


