# 83.Recursive function
def factorial(n):
    if n==1:
        return n
    else:
        return n * factorial(n-1)
    
num=int(input('Enter the number to find factorial: '))
result=factorial(num)
print(f"The factorial {num} is {result}")
        