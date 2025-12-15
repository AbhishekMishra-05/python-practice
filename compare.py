x=int(input("enter the value of x: "))
y=int(input("enter the value of y: "))

if x<y:
    print(f"{x} is less than {y}")
    print("x is less than y")
elif x>y:
    print(f"{x}is greater then {y}")
    print("x is greater than y")

# elif x==y:
else:
    print(f"{x} is equal to {y}")
    print("x is equal to y")

