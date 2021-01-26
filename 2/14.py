print("Input number. Takes input and displays line X from the beginning.")
num = int(input())
with open("./popular-names.txt", "r") as rf:
    data = rf.readlines()[0:num]

for i in data:
    print(i, end="")
