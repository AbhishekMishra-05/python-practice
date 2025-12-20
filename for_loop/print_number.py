# # Print numbers from 1 to 10 using for

for i in range (1,10):
    print(i, sep="\n")



# #Print numbers from 1 to 10 using while 

num=int(input("Enter a number:" ))

while num<=10:
    print(num)
    num+=1



# Print even numbers between 1 and 50

def number():
    for i in range (1,51):
        if i%2==0:
            print(i)
number()




#  take the starting point by user input

def even():
    start=int(input("Enter the start point:"))
    end=int(input("Enter the end point:"))

    for _ in range (start, end+1):
        if _%2 ==0:
            print(_)
even()

