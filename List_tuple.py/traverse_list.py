# Create a list and print it

names=["Abhishek","Mishra","Me"]
num=[1,2,8,4,6]
print(f"current list:{names} and {num}")

# Add elements to a list
names.append("Tudu")
num.append(6)
print(f"After append:{names} and {num}")

# Sort a list
names.sort()
num.sort()
print(f"The sorted list are :{names} and {num}")

# Remove elements from a list
names.pop(1)
num.pop(1)
print(f"After removing:{names} and{num}")

# Find length of a list
print(len(names), end =" ")
print(len(num), end="\n")

# Access list elements
# printing last index value
print(names[-1])
print(num[-1])

#  using for loop to print values
for i in names:
    print(i)
for j in num:
    print(j)


# Find max and min in a list
biggest=num[0]
smallest=num[0]
for i in num:
    if i>=biggest:
        biggest=i
    if i<=smallest:
        smallest=i
print(f"The smallest number is:{smallest}")
print(f"The maximum value is:{biggest}")

# Sum all elements in a list
Total=0
for i in num:
    Total+=i
print(f"The Total of list is:{Total}")


# Remove duplicates from a list
# i=0
# while i < len(num):
#     j=i+1
#     while j< len(num):
#         if num[i]==num[j]:
#             num.pop(j)
#         else:             
#             j+=1
#     i+=1
# print(f"The list after duplicated removal is: {num}")

# Another approach
unique=[]
for i in num:
    if i not in unique:
        unique.append(i)
print(f"The original list is:{num}")
print(f"The duplicated removed list is:{unique}")


#Find second largest number in a list
largest=num[0]
second_largest=float('-inf')
for i in num:
    if i > largest:
        second_largest=largest
        largest=i
    elif i< largest and i> second_largest:
        second_largest=i
print(f"The original list is:{num}")
print(f"The second largest={second_largest}")


# Reverse a list

rev=[]
counter=len(num)-1
while counter>=0:
        rev.append(num[counter])
        counter-=1
print(f"The reversed list is:{rev}")
    
# another approach

# Reverse a list using for loop
rev = []

for i in range(len(num) - 1, -1, -1):
    rev.append(num[i])

print(f"The reversed list is: {rev}")



# Count occurrences of an element

count=0

element=int(input("Enter element to count: "))
for i in num:
    if i==element:
        count+=1
if count ==0:
    print("Element not found")
else:
    print(f"{element} has occurance {count}")
