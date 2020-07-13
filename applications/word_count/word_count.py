def word_count(s):
    # $%$Start
    tr = str.maketrans('', '', '":;,.-+=/\\|[]{}()*^&')
    s = s.translate(tr).lower()

    words = s.split()
    counts = {}

    for w in words:
        if w not in counts:
            counts[w] = 1
        else:
            counts[w] += 1

    return counts
    # $%$End


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))