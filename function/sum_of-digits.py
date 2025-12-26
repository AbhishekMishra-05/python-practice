# recursion problem
def sum_of_digits(num):
    if num==0:
        return num
    else:
        last_digit= num %10
        remaining=num//10
        return last_digit + sum_of_digits(remaining)
number=int(input("Enter the digits to find sum:"))
result=sum_of_digits(number)
print(f"The sum of digits are:{result}")

        
