#  weight converting using of def functions( with opps)
weight = float(input("Enter your weight: "))
unit = input("Enter the unit: ")


def lbs_to_kg():
    converted = weight * 0.453592
    return converted


kg = lbs_to_kg()


def kg_to_lbs():
    converted = weight / 0.453592
    return converted


lbs = kg_to_lbs()


def calculation():
    if unit.upper() == "L":
        print(f"your weight is {kg} kilos")
    elif unit.upper() == "K":
        print(f" your weight is {lbs} lbs")
    else:
        print("sorry!! wrong unit")


calculation()

