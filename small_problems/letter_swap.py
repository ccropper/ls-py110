def swap(words):
    words = words.split()
    results = []
    for word in words:
        if len(word) > 1:
            results.append(word[-1] + word[1:-1] + word[:1])
        else:
            results.append(word)

    reversed = " ".join(results)

    return reversed


print(swap("Oh what a wonderful day it is") == "hO thaw a londerfuw yad ti si")  # True
print(swap("Abcde") == "ebcdA")  # True
print(swap("a") == "a")  # True
