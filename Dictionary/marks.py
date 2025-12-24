# 70.Find student marks using dictionary

marks={
    "dbms":80,
    "os":90,
    "math":85
}
for key,value in marks.items():
    print(f"{key:<12}--> {value}")

print(marks["dbms"])


# 71.Sort dictionary by keys
sorted_keys = sorted(marks)
for key in sorted(marks):
    print(key, marks[key])


# Sort dictionary by keys
sorted_values = sorted(marks.values())
print(sorted_values)

# sorting complete dictionary by keys
sort_dict=dict(sorted(marks.items()))
print(sort_dict)

# sorting complete dictionary by values
sort_dict = dict(sorted(marks.items(), key=lambda x: x[1]))
print(sort_dict)
