# cut -f 1 popular-names.txt |sort|uniq -c|sort -r
names = []
with open("popular-names.txt", "r") as rf:
    for line in rf:
        data = line.split("\t")
        names.append(data[0])
dic = {}
for i in set(names):
    dic[i] = names.count(i)
dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
for j in dic:
    print(j)
