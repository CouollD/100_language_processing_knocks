import json

# title ="イギリス"の行を出力する
with open("jawiki-country.json", "r") as rf:
    # lineごとに読み込みを行うので、jsonファイルを下手に整形すると読み取れない。
    for line in rf:
        line = json.loads(line)
        if line['title'] == "イギリス":
            result = line['text']
print(result)

with open("./result/output20.txt", "w") as wf:
    wf.write(result)
wf.close
