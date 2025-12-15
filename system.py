
# using excepton handling
import sys
try:    
    print("hello,my name is,",sys.argv[1])
except IndexError:
    print("error coming")


# using sys.exit and if else ladder
import sys
if len(sys.argv) < 2:
    sys.exit("too few arguments")
elif len(sys.argv) > 10:
    sys.exit("too many arguments")

print("Hello, my name is:", sys.argv[1])


# if you want to print all arguments passed except the script name
import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# if output required in different lines
print("You entered:")
for arg in sys.argv[1:]:
    print(arg)

# # if output required in one line
print( " ".join(sys.argv[1:]))
