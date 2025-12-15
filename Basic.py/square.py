def main():
    num= int(input("Enter the number of which you want square and cube:"))
    print(f"The cube is: {cube(num)}")
    print(f"The square is: {square(num)}")
def square(n):
    return pow(n,2)
def cube(n):
    return pow(n,3)
if __name__ == "__main__":
    main()