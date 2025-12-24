# 73. What is a Function?
# A function is a block of reusable code that performs a specific task.
# Instead of writing the same code again and again, we put it inside a 
# function and call it whenever needed

# 74.Create a simple function

def age(n):
    if n>=18:
        print("adult")
    else:
        print("minor")
age(19)

# 75.Function with parameters
def area(a):
    return a**2
print(area(4))


# 76.Function with return value
def area_reactangle(l,b):
    return l * b
print(f"the area of rectangle is:{area_reactangle(5,4)}")


# 77.Check even or odd using function
def even_odd():
    try:
        
        num=int(input("Enter a number: "))
        if num ==0:
            print("can't be determined")
        elif num % 2 ==0:
            print(f"The entered number is even:{num}")
        else:
            print(f"The entered number is odd:{num}")
    except ValueError:
        print("Invalid input")

even_odd()


# 78.Find factorial using function
def factorial():
    n=int(input("Enter the number:"))
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(f"The factorial of number is:{factorial()}")


# 79.Find maximum of two numbers using function
def find_max(a,b):
    return a if a>=b else b
print(f"The max number is:{find_max(4,3)}")


# 80.Function to reverse a string
def reverse_string():
    word="Abhishek"
    
    # using for loop you should always give start, stop,jump
    print("Using for loop:\n")
    for i in range (len(word)-1,-1,-1):
        print(word[i],end="")

    # using while loop
    print("\nUsing while loop:")
    i=len(word)-1
    while i>=0:
        print(word[i], end="")
        i-=1
reverse_string()



   
