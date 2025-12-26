# remove duplicate characters

name = input("Enter the string: ").lower()

seen = set()
result = ""

for ch in name:
    if ch not in seen:
        result += ch
        seen.add(ch)

print("After removing duplicates:", result)
