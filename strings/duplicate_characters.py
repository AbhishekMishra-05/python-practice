# 88. Find duplicate characters
name = input("Enter the string: ").lower()
store={}
for ch in name:
    if ch in store:
        store[ch]+=1
    else:
        store[ch]=1
print(store)
for ch, count in store.items():
    if count > 1:
        print(ch,"->", count)


