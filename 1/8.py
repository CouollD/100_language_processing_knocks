def cipher(sentence: str) -> str:
    result = ""
    for i in range(len(sentence)):
        target = sentence[i]
        if target.islower():
            target = chr(219 - ord(target))
        result += target
    return result


print(cipher("I am a Hero."))
