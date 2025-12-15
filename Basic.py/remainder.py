# Find the remainder of a division
def remainder():
    try:
        divisor =int(input("enter the divisor:" ))
        dividend=int(input("Enter the dividend: "))
        remainder = dividend % divisor
        print(f"{remainder} is the result.")
    except ValueError:
        print("Invalid input")
    except ZeroDivisionError:
        print("Divisor cannot be zero.")
remainder()