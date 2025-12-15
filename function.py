def hello(to="world"):
    print("hello,",to)
hello()

name=input("Enter your name:? ").strip().title()
hello(name)
# print(f"Hello, {name}!")