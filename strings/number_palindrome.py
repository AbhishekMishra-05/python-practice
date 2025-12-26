# check number is palindrome or not
def palindrome():
    num = int(input("Enter the value: "))

    if num < 0:
        print("Negative numbers are not palindromes")
        return
    
    original_num = num
    rev =  0

    while num>0:
        last_digit= num % 10
        rev= rev*10+last_digit
        num = num//10

    if original_num == rev:
        print(f"The num is palindrome number\n {original_num} = {rev}")
    else:
        print("Not a palindrome")

palindrome()

        

           
    

