name=input("enter your name:")
file=open("names.txt","a")
file.write(f"{name}\n")
file.close()



# now using loops
# with open("names.txt","a") as file:
#         for _ in range(5):
#             name=input("enter your name:")
#             file.write(f"{name}\n")
            