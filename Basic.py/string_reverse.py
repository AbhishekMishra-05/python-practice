# Reverse a string
def reverse():
    word = "reversing"
    counter = len(word)-1
   

    # printing the reverse character of string with index

    while counter>=0:
        print(counter,word[counter])
        counter-=1
     

    # Printing a reversing string
    
    rev=""
    while counter>=0:
        rev+=word[counter]
        counter-=1
    print(f"The reverse string is:{rev}")

reverse()
