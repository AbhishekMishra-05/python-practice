# 61.Create a dictionary

information = {
    "name": "Abhishek",
    "age": 22,
    "address": "Nepal",
    "degree": "B.Tech, CSE",
    "contact_no": "7205575138",
    "email": "abhishekmishra26789@gmail.com"
}
for key,value in information.items():
    print(f"{key:<12}--> {value}")


# 62.Access dictionary values
print(information["name"])
print(information.get("age"))
print(list(information.keys()))
print(list(information.values()))
print(list(information.items()))

# 63.Add new key-value pairs
information.update({
    "state":"madhesh",
})
# 64.Update dictionary values
information["contact_no"] = ["7205575138"]
information["contact_no"].append("7753047820")
for key,value in information.items():
    print(f"{key:<12}--> {value}")


# 65.Delete elements from dictionary
print("Before deletion:")
for key,value in information.items():
    print(f"{key:<12}--> {value}")

information["contact_no"].remove("7753047820")
del information["state"]

print("\nAfter deletion:")
for key,value in information.items():
    print(f"{key:<12}--> {value}")


# 66.Loop through dictionary keys
for i in information.keys():
    print(i)

# 67.Loop through dictionary values
for j in information.values():
    print(j)

# 68.Count frequency of characters in a string
name=information["name"]
freq={}
for ch in name:
    freq[ch]=freq.get(ch,0)+1
for key,value in freq.items():
    print(key,"-->",value)


# counting frequency of each string and list present in dictionary
fre={}
for value in information.values():
    if isinstance(value,str):
        for ch in value:
            fre[ch]=fre.get(ch,0)+1

    elif isinstance(value,list):
        for item in value:
            for ch in item:
             fre[ch]=fre.get(ch,0)+1
for key,value in fre.items():
    print(key,"-->",value)


# 69.Count frequency of words in a dictionary
information.update({
    "feeling":"I love python and I love coding"
})
sentence=information["feeling"]
freq={}
for value in information.values():
    if isinstance(value,str):
        words = value.lower().split()
        for word in words:
         freq[word]=freq.get(word,0)+1
for key,value in freq.items():
    print(f"{key} -->{value}")



# for counting frequency of particular key value
sentence=information["feeling"]
freq={}
words = sentence.lower().split()
for word in words:
    freq[word]=freq.get(word,0)+1
for key,value in freq.items():
    print(f"{key} -->{value}")