str0 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
list0, dict0 = [1, 5, 6, 7, 8, 9, 15, 16, 19], {}
data = str0.split(" ")
for i in range(len(data)):
    num = i + 1
    if num in list0:
        dict0[data[i][:1]] = num
    else:
        dict0[data[i][:2]] = num
dic = sorted(dict0.items(), key=lambda x: x[1])
print(dict0)
print(dic)
