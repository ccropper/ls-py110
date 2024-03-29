"""

Given a list of strings, return a new list where the strings are sorted based on the highest number of adjacent consonants a string contains. 

###################

P - PROBLEM

###################

Input:
    - A list of strings
        - may contain spaces

Output:
    - A NEW list of strings, sorted based on the spec

Explicit requirements:
    - If two strings contain the same highest number of adjacent consonants, they should retain their original order in relation to each other. 
    - Consonants are considered adjacent if they are next to each other in the same word or if there is a space between two consonants in adjacent words.

Implicit requirements:
    - there may be more than one word per string
    - 


Questions: 
    - what happens when the string is empty
    - what happens if there a string contains no consonants?
    - should this function be internationalized?
    - does capitalization matter?
    - what about if consonants are separated by punctuation?
    - (missed) should the string be sorted in ascending or descending order? (I had assumed ascending)


###################
    
E - EXAMPLES

###################

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

Updates to implicit requirements:
    - can contain more than one word
    - still not sure if capitalization matters, but if we just need to pass test cases then case doesn't matter (all inputs are lowercase)
    - not sure how to handle punctuation
    - not sure what to do if string is empty
    - if string contains no consonants, it is treated the same as if there is only one consonant (retain order)
    - sort in descending order


###################
    
D - DATA STRUCTURES

###################

- we need to maintain order, so lists are handy here
- (missed) maybe a dictionary to keep track of how many consequective consonants are in each string
    - as of python3.7, dictionaries maintain order of insertion


###################
    
A - ALGORITHM

###################

- take a list of string as input
- create a results list to receive strings based on their sorting
- create a dictionary, consecutive_consonants_dict where the key is the string and the value is the number of consecutive consonants it has
- iterate over the list of strings
    - for each string, call count_consecutive_consonants() and store the result in consecutive_consonants_dict as the value to the key of the string

- split consecutive_consonants_dict into two dicts:
    - one where values > 1
    - one where values =< 1

loop through consecutive_consonants_dict where values > 1:
    - sort the dict by value in descending order
    - append the key to the results list

loop through consecutive_consonants_dict where values =< 1:
    - append the key to the results list

return results list

-------

mini-PEDAC for count_consecutive_consonants():

### P ###

input: a string that may contain spaces
output: an integer representing the number of consecutive consonants in the input string

### E ###

examples:

count_consecutive_consonants('aa') == 0
count_consecutive_consonants('baa') == 1
count_consecutive_consonants('ccaa') == 2
count_consecutive_consonants('dddaa') == 3

### D ###

- need a frozenset of consonants (?)

### A ###

strip the spaces out of words
set var consecutive_consonants = ''
set var max_consecutive_consonants = 0

for character in string:
    if is_consonant(character):
        add character to consecutive consonant
    else:
        if len(consecutive_consonants) > max_consecutive_consonants:
            max_consecutive_consonants = len(consecutive_consonants)
        consecutive_consonants = ''

return max_consecutive_consonants

### C ###

def is_consonant(char):
    return char in set('bcdfghjklmnpqrstvwxyz')


def count_consecutive_consonants(str):
    consecutive_consonants = ''
    max_consecutive_consonants = 0

    for char in str:
        if is_consonant(char):
            consecutive_consonants += char
        else:
            if len(consecutive_consonants) > max_consecutive_consonants:
                max_consecutive_consonants = len(consecutive_consonants)
            consecutive_consonants = ''

    return max_consecutive_consonants


-------

###################
    
C - CODE






###################   

"""


def is_consonant(char):
    return char in set("bcdfghjklmnpqrstvwxyz")


def count_max_adjacent_consonants(str):
    str = str.replace(" ", "")
    consecutive_consonants = ""
    max_consecutive_consonants = 0

    for char in str:
        if is_consonant(char):
            consecutive_consonants += char
            if (
                len(consecutive_consonants) > 1
                and len(consecutive_consonants) > max_consecutive_consonants
            ):
                max_consecutive_consonants = len(consecutive_consonants)
        else:
            if (
                len(consecutive_consonants) > 1
                and len(consecutive_consonants) > max_consecutive_consonants
            ):
                max_consecutive_consonants = len(consecutive_consonants)
            consecutive_consonants = ""

    return max_consecutive_consonants


# test cases

# print(count_max_adjacent_consonants('dddaa'))       # 3
# print(count_max_adjacent_consonants('ccaa'))        # 2
# print(count_max_adjacent_consonants('baa'))         # 0
# print(count_max_adjacent_consonants('aa'))          # 0
# print(count_max_adjacent_consonants('rstafgdjecc')) # 4

# debugging test case

# print(count_max_adjacent_consonants('month'))       # 3


def sort_by_consonant_count(strings):
    strings.sort(key=count_max_adjacent_consonants, reverse=True)
    return strings


"""
- take a list of string as input
- create a results list to receive strings based on their sorting
- create a dictionary, consecutive_consonants_dict where the key is the string and the value is the number of consecutive consonants it has
- iterate over the list of strings
    - for each string, call count_consecutive_consonants() and store the result in consecutive_consonants_dict as the value to the key of the string

- split consecutive_consonants_dict into two dicts:
    - one where values > 1
    - one where values =< 1

loop through consecutive_consonants_dict where values > 1:
    - sort the dict by value in descending order
    - append the key to the results list

loop through consecutive_consonants_dict where values =< 1:
    - append the key to the results list

return results list]
"""


my_list = ["aa", "baa", "ccaa", "dddaa"]
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ["can can", "toucan", "batman", "salt pan"]
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ["bar", "car", "far", "jar"]
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ["day", "week", "month", "year"]
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ["xxxa", "xxxx", "xxxb"]
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']
