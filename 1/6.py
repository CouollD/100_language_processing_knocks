def make_char_ngram(sentence: str, num: int) -> list:
    str0, result = sentence.replace(" ", ""), []
    for i in range(len(str0) - num + 1):
        result.append(str0[i:i + num])
    return result


str1, str2 = "paraparaparadise", "paragraph"
X, Y = set(make_char_ngram(str1, 2)), set(make_char_ngram(str2, 2))
union, intersection, dif = X.union(Y), X.intersection(Y), X.difference(Y)
print(union, "\n", intersection, "\n", dif)
print(bool("se" in X))
print(bool("se" in Y))
