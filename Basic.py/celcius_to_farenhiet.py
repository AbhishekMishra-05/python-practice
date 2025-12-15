def celsius():
    try:
        cel=float(input("Enter temperature in Celsius:"))
        farenheit=(cel*9/5)+32
        print(f"The {cel}C temperature in Farenheit is: {farenheit}F")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
celsius()