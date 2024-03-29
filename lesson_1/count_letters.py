statement = "The Flintstones Rock"


def count_letters(statement):
    statement = statement.replace(" ", "")
    letter_count = {}
    for letter in statement:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count


print(count_letters(statement))

# Pretty printed for clarity

# {
#     'T': 1,
#     'h': 1,
#     'e': 2,
#     'F': 1,
#     'l': 1,
#     'i': 1,
#     'n': 2,
#     't': 2,
#     's': 2,
#     'o': 2,
#     'R': 1,
#     'c': 1,
#     'k': 1
# }

"""
LS solution uses:

for char in statement:
    char_freq[char] = char_freq.get(char, 0) + 1

"""