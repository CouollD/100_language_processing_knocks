# cut -f 3 popular-names.txt | sort
names = []
with open("popular-names.txt", "r") as rf:
    for line in rf:
        data = line.split("\t")
        names.append(int(data[2]))
names = sorted(names)
for i in names:
    print(i)
