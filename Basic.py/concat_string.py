# Concatenate two strings
def concat():

    # declaration of two strings
    first_name="Abhishek"
    last_name="Mishra"

    # concatination of string and storing in a variable
    full_name = f"{first_name} {last_name}"

    # concatination of string in three ways
    print(f"{first_name} {last_name}")
    print(first_name + " " + last_name)
    print(" ".join([first_name,last_name]))

    #  printing the length and concatinated string 
    print(f"the length of string is:",len(full_name),full_name)

# calling the concat function
concat()