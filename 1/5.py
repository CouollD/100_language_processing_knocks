def make_char_ngram(sentence: str, num: int) -> list:
    str0, data = sentence.replace(" ", ""), []
    for i in range(len(str0) - num + 1):
        data.append(str0[i:i + num])
    return data

def make_voc_ngram()


str0 = "I am an NLPer"
data = makeNgram(str0, 2)
print(data)
