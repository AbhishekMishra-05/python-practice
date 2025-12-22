# Find factorial of a number
try:
    num=int(input("Enter the number:" ))
    if num==0:
        print("cannot do factorial")
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(f" the factorial of {num} is:{fact}")
except ValueError:
    print("invalid")
