import random

list = ["Wrath", "Lust", "Sloth", "Greed", "Envy", "Pride", "Gluttony"]
list2 = list

list3 = []
X = 1
for i in list:
    for ii in list2:
        if i != ii:
            t = f"{X}. {i}-{ii}"
            list3.append(t)
            X += 1

for t in list3:
    print(t)