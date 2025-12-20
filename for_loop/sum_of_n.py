# Find the sum of first N numbers and sum first N odd numbers and even numbers

def num_sum():
    num=int(input("Entr the number: "))

    # sum of n first n number
    s = num*(num+1)//2

    #  sum of n odd number
    odd= num**2

    # sum of n even  number
    even_sum = num * (num + 1)

    print(f"The sum of number is:{s}")
    print(f"The sum of number is:{odd}")
    print(f"The sum of number is:{even_sum}")

num_sum()



# sum of the number upto given limit

def limit():
    n=int(input("Entr the number: "))

    total_sum=0
    odd_sum=0
    even=0

    for i in range (0,n+1):
        total_sum += i

        if i%2==0:
            even+=i
        else:
            odd_sum+=i

    print(f"The sum of total number is:{total_sum}")
    print(f"The sum of odd number is:{odd_sum}")
    print(f"The sum of even number is:{even}")

limit()