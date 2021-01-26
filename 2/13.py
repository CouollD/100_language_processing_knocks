def readFile(filename):
    myfile = open(filename, "r")
    data = myfile.readlines()
    myfile.close()
    return data


col0 = readFile("./result/col0.txt")
col1 = readFile(".result//col1.txt")

with open("./result/test13.txt", "w") as wf:
    for i in range(len(col0)):
        wf.write(col0[i].replace("\n", "\t") + col1[i])
