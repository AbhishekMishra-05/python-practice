# 87.Check if string is palindrome
name="madam"
i =len(name)-1
result=""
while i>=0:
    result += name[i]
    i-=1
if name == result:
    print(f"\nIt is a palindrome: \n{name} = {result}")
else:
    print("\nNot a palindrom")