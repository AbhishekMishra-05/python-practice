# Check if a year is a leap year
def leap_year():
    year=int(input("Enter the year: "))

    # if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    if year % 400 == 0:
        print(f"{year} is a leap year")
    elif year % 100 == 0:
        print(f"{year} is not a leap year")
    elif year % 4 == 0:
        print(f"The year {year} is a leap year")
    else:
        print("Not a leap year")
leap_year()

