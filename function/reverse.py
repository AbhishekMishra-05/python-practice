# reverse number using recursion
def reverse_num(n, rev=0):
    if n == 0:
        return rev
    else:
        last_digit = n % 10
        new_rev = rev * 10 + last_digit
        remaining = n // 10
        return reverse_num(remaining, new_rev)
        # return reverse_num(n // 10, rev * 10 + last_digit)
num = int(input("Enter the number: "))
result = reverse_num(num)
print(f"The reverse number is: {result}")

    