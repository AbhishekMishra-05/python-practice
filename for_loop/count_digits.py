# Count digits in a number
try:
    num=int(input("Enter the number:" ))
    count =0
    if num==0:
        count=1
    else:
        while num!=0:
            count+=1
            num//=10
    print(count)
except ValueError:
    print("invalid input")
    