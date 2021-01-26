# cut -f 1 popular-names.txt |sort|uniq|wc
# 先頭だけ配列に格納
names = []
with open("popular-names.txt", "r") as rf:
    for line in rf:
        data = line.split("\t")
        names.append(data[0])
print(len(set(names)))
