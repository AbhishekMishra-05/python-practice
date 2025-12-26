# 84.Find Fibonacci using recursion
def fibonacci(n,a=0,b=1):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return  fibonacci(n - 1) + fibonacci(n - 2)
    
num = int(input("Enter a number: "))
result = fibonacci(num)
print(f"Fibonacci of {num} is {result}")
    
   
   
# fibonacci using iteration
#     for _ in range (n):
#         print(a, end="")
#         next= a+b
#         a=b
#         b=next

# fibonacci(5)
