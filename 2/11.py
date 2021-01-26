# ファイルを開く
with open("./reslut/test11.txt", "w") as wf:
    with open("/Users/nishimurachieko/Documents/1000本ノック/2/popular-names.txt", "r") as rf:
        for data in rf:
            wf.write(data.strip().replace("\t", " "))
