try:
    num = int(input("Enter the number to check: "))

    if num > 0:
        print(f"{num} is a positive number.")
    elif num < 0:
        print(f"{num} is a negative number.")
    else:
        print("The number is zero.")

except ValueError:
    print("Invalid input, please enter a numeric value.")
