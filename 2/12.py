col = [[], [], [], []]
with open("/Users/nishimurachieko/Documents/1000本ノック/2/popular-names.txt", "r") as rf:
    for line in rf:
        line = line.replace("\n", "")
        data = line.split("\t")
        for i in range(4):
            col[i].append(data[i])
length = len(col[0])

for i in range(4):
    txtname = "./reslut/col" + str(i) + ".txt"
    with open(txtname, "w") as wf:
        for j in range(length):
            wf.write(col[i][j] + "\n")
