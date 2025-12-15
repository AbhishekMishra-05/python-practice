# convert miles to kilometers
def mile_to_km():
    try:
        miles = float(input("Enter distance in miles: "))
        kilometer = miles * 1.60934
        print(f"{miles} mile is equal to {kilometer} kilometers")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


# convert kilometers to miles
def km_to_miles():
    try:
        km = float(input("Enter distance in km: "))
        mile = km / 1.60934
        print(f"{km} kilometer is equal to {mile} miles")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


def main():
    mile_to_km()
    km_to_miles()


if __name__ == "__main__":
    main()




# menu driven program 

def mile_to_km(miles):
    return miles * 1.60934


def km_to_miles(km):
    return km / 1.60934


def main():
    print("1. Miles to Kilometers")
    print("2. Kilometers to Miles")

    choice = input("Enter your choice (1 or 2): ")

    try:
        if choice == "1":
            miles = float(input("Enter miles: "))
            print("Kilometers:", mile_to_km(miles))

        elif choice == "2":
            km = float(input("Enter kilometers: "))
            print("Miles:", km_to_miles(km))

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter a valid number")


if __name__ == "__main__":
    main()
