def odd_even():
    try:
        num = int(input("Enter the number to check: "))
        
        if num == 0:
            print("The number is zero.")
        elif num % 2 == 0:
            print(f"{num} is an even number.")
        else:
            print(f"{num} is an odd number.")
            
    except ValueError:
        print("Invalid input, please enter a numeric value.")

odd_even()
