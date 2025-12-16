# prime number check
def prime():
    num=int(input("Enter the number to check:"))

    if num <=1:
        print("it is not a prime number")
        return

    for i in range(2,num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            return 
        
    print(f"{num} is a prime number")
prime()



#  program to print prime number

# print()
def print_primes():
    n = int(input("Enter the limit: "))

    for num in range(2, n + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:   # this else belongs to the inner for-loop
            print(num)

print_primes()
