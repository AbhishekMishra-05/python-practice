#  Find the largest of two numbers
def find_largest():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if a > b:
            print(f"{a} is the largest number.")
        elif b > a:
            print(f"{b} is the largest number.")
        else:
            print("Both numbers are equal.")

    except ValueError:
        print("Invalid input! Please enter integers only.")

find_largest()




# Find the largest of three numbers

def largest():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        c = int(input("Enter third number: "))

        if a >= b and a >= c:
            print(f"{a} is the largest number.")
        elif b >= a and b >= c:
            print(f"{b} is the largest number.")
        else:
            print(f"{c} is the largest number.")
    except ValueError:
        print("Invalid input! Please enter integers only.")

largest()
