# sort the list so that the sub-lists are ordered based on the sum of the odd numbers that they contain. You shouldn't mutate the original list.

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def sum_of_odd_numbers(lst):
    return sum([number for number in lst if number %2 != 0])

print(sorted(lst, key=sum_of_odd_numbers)) # [[1, 8, 3], [1, 6, 7], [1, 5, 3]]