str1, str2, str3 = "パタトクカシーー", "パトカー", "タクシー"
print(str1[::-1])
print(str1[0] + str1[2] + str1[4] + str1[6])
str4 = ""
for i in range(4):
    str4 += str2[i]
    str4 += str3[i]
print(str4)
