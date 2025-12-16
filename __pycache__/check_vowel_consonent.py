# 32.Check if a character is a vowel or consonant
def vowel():
    v = input("Enter the character: ").lower()
    word = ['a', 'e', 'i', 'o', 'u']

    if len(v) !=1:
        print("invalid input")
    elif not v.isalpha():
        print("invalid input")
    elif v in word:
        print(f"{v} Vowel")
    else:
        print(f"{v} consonent")

vowel()


