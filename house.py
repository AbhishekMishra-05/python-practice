name=input("Enter your name:? ")
# if name=="Anhishek":
#     print("radhemai")
# elif name=="pramod":
#     print(" radhemia")
# else:
#     print("who?")
match name:
    case "Abhishek":
        print("radhemai")
    case "pramod":
        print(" radhemia")
    case _:
        print("who?")