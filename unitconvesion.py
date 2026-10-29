# Unit Conversion System

def length(km):
    return km * 0.621371

def weight(kg):
    return kg * 1000

def temperature(c):
    return (c * 9 / 5) + 32

def time_convert(hours):
    return hours * 60


while True:
    print("\n--- UNIT CONVERSION SYSTEM ---")
    print("1. Length (KM to Miles)")
    print("2. Weight (KG to Grams)")
    print("3. Temperature (C to F)")
    print("4. Time (Hours to Minutes)")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "0":
        print("Thank you!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Select 1 to 4.")
        continue

    try:
        value = float(input("Enter value: "))

        if choice == "1":
            print(f"{value:g} km = {length(value):.2f} miles")

        elif choice == "2":
            print(f"{value:g} kg = {weight(value):.2f} g")

        elif choice == "3":
            print(f"{value:g} C = {temperature(value):.2f} F")

        elif choice == "4":
            print(f"{value:g} hours = {time_convert(value):.2f} minutes")

    except ValueError:
        print("Invalid value. Enter a number.")