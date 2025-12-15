# with open("names.txt","r")as file:
#     lines=file.readlines()
#     for line in sorted(lines):
#         print(line.rstrip())


# other way
names = []
with open("names.txt","r")as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"{name}")