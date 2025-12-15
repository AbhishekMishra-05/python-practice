#Access a character from a string 
def character():
    char=[]
    letter="sentence"

    # Append each character to the list and then print each character
    for  ch in letter:
        char.append(ch)

        # reading character along with index and printing from list
    for index,ch in enumerate (char):
        print(index,ch)

    # not appending to the list directly printing along with yhe index
    for i,ch in enumerate(letter):
        print(i,ch)
character()



# direct access to the character usingg print and index

def char():
    word="string"
    for w in word:
        print(w)
char()