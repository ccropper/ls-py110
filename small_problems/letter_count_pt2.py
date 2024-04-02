"""
### P
Write a function that takes a string consisting of zero or more space-separated words and returns a dictionary that shows the number of words of different sizes.

Input: a string broken up by spaces
Output: a dictionary

Explicit Requirements:
- Words consist of any sequence of non-space characters.
- don't count non-letters when determining word size

### E 

see test cases

new knowledge: 
- return empty dictionary if empty string passed in

### D

a list to hold the words in
dict to return things in

### A

split string into a list of words based on space as a delimiter
create a results dict

loop through list of words
    if the length of the word already exists as a key
        add 1 to the value
    else
        create a new key:value pair with length of word as key and 1 as value


### C 

see below

"""

def clean_string(string):
    clean_string = ''

    for char in string:
        if char.isalpha():
            clean_string += char

    return clean_string
    

def word_sizes(string):
    results = {}
    words = string.split()

    for word in words:
        word = clean_string(word)
        if len(word) in results.keys():
            results[len(word)] += 1
        else:
            results[len(word)] = 1

    return results

    pass

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})