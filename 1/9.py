import random


def random_vocab_arrange(sentence: str) -> str:
    data = sentence.split(" ")
    data.remove(".")
    num = len(data) - 1
    if num > 3:
        # 最初と最後意外がランダムなインデックス配列
        result = [0]
        numbers = list(range(1, num))
        random.shuffle(numbers)
        result.extend(numbers)
        result.append(num)
        result_str = ""
        for i in result:
            result_str += data[i] + " "
    else:
        result_str = sentence
    return result_str + "."


str0 = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
# str0 = "I have a pen"
print(random_vocab_arrange(str0))
