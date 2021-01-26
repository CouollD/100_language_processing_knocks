def make_char_ngram(sentence: str, num: int) -> list:
    str0, result = sentence.replace(" ", ""), []
    for i in range(len(str0) - num + 1):
        result.append(str0[i:i + num])
    return result


def make_voc_ngram(sentence: str, num: int) -> list:
    data, result = sentence.split(" "), []
    for i in range(len(data) - num + 1):
        result.append([data[i], data[i + 1]])
    return result


str0 = "I am an NLPer"
data1, data2 = make_char_ngram(str0, 2), make_voc_ngram(str0, 2)
print(data1, data2)
