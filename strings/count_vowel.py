# 86.Count vowels in a string
name=input("Enter the string: ").lower()
vowel={'a','e','i','o','u'}
count=0
for ch in name:
    if ch in vowel:
        print(f"This is vowel {ch}")
        count+=1
    else:
        print(f"This is consonent { ch}")

print(f"The total number of vowel count is {count}")