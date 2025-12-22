# 41.Print Fibonacci series
number=int(input("enter the number:"))
first=0
second=1
for i in range(number):
    print(f"{first}", end=" ")
    next=first+second
    first=second 
    second=next
