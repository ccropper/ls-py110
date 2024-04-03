def is_palindrome(string):
    string = str(string)
    return string == string[::-1]


def is_real_palindrome(string):
    case_insensitive_string = string.casefold()
    cleaned_string = ""

    for char in case_insensitive_string:
        if char.isalnum():
            cleaned_string += char

    return is_palindrome(cleaned_string)


print(is_real_palindrome("madam") == True)  # True
print(is_real_palindrome("356653") == True)  # True
print(is_real_palindrome("356635") == False)  # True
print(is_real_palindrome("356a653") == True)  # True
print(is_real_palindrome("123ab321") == False)  # True

# case doesn't matter
print(is_real_palindrome("Madam") == True)  # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True)  # True
