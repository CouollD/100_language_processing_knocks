print("Input number. Takes input and displays the last X lines.")
num = int(input())
with open("./popular-names.txt", "r") as rf:
    data = rf.readlines()[-num:]

for i in data:
    print(i, end="")
