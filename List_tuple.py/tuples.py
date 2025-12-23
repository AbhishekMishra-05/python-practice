# 54.Create a tuple
tup1=("Abhishek","Mishra")
tup2=(1,2,3,4,5,6)

# 55.Convert list to tuple
names=["Abhishek","Mishra","Me"]
tup3=tuple(names)
print(f"{tup1}\n{tup2}\n{tup3}")


# 56.Access tuple elements
print(tup1[0])
print(tup2[-1])
print(tup3[2])




# 57.Sets
my_set={"Abhishek","Mishra",1,2,3,8}
print(my_set)


# 58.Add and remove elements from a set
my_set.add("Tudu")
my_set.add(4)
my_set.update([5,6,7])
print(my_set)


# 59.Find union and intersection of two sets
A={1,2,3,4}
B={3,4,5,6}

union=set()
for i in A:
    union.add(i)
for i in B:
    if i not in union:
        union.add(i)
print(f"The union is:{union}")

# another way to find union
union=A|B
print(f"The union is:{union}")

# another way to find union
union_set=A.union(B)
print(f"The union is:{union}")

# Intersection
intersection=set()
for i in A:
    if i in B:
        intersection.add(i)

print(f"The intersection is:{intersection}")

# anotherway
intersection=A & B
print(f"The intersection is:{intersection}")

# another way
intersection=A.intersection(B)
print(f"The intersection is:{intersection}")