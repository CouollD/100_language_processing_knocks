# コマンドラインでできないので、一旦保留
import numpy as np
print("Input number. Divide the list by the numbers entered.")
num = int(input())

with open("./popular-names.txt", "r") as rf:
    data = rf.readlines()

result = list(np.array_split(data, num))
for i in range(num):
    txtname = "./result/split" + str(i + 1) + ".txt"
    with open(txtname, "w") as wf:
        for j in range(len(result[i])):
            wf.write(result[i][j] + "\n")
