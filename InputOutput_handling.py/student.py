# students=[]
# with open("students.csv") as file:
#     for line in file:
#         name,house=line.rstrip().split(",")
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)





# other approach using csv module

# students=[]
# with open("students.csv") as file:
#     for line in file:
#         name,house=line.rstrip().split(",")
#         student={"name":name,"house":house}
#         students.append(student)
# for student in sorted(students,key=lambda student:student["name"]):
#     print(f"{student['name']} is in {student['house']}") 




#  other approach using CSV module

# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})
# for student in sorted(students,key=lambda student:student["name"]):
#     print(f"{student['name']} is in {student['home']}")


# for writing to csv file
import csv
name=input("Name:")
home=input("Home:")

with open("students.csv","a",newline="") as file:
    writer=csv.DictWriter(file ,fieldnames=["name","home"])
    writer.writerow({"name":name,"home":home})
