students=["Alice", "Bob", "Charlie", "David"]
# for i in range (len(students)):
#     print(i+1,students[i])
for index, student in enumerate(students, start=1):
    print(index, student)