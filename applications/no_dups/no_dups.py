def no_dups(s):
    # $%$Start
    words = s.split()

    seen = {}
    result = []

    for w in words:
        if w not in seen:
            result.append(w)
            seen[w] = True

    return " ".join(result)
    # $%$End


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))