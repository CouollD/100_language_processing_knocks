str0 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
data = str0.split(" ")
data2 = []
for i in data:
    data2.append(len(i))
print(data2)
