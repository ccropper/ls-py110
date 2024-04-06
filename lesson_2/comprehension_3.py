lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# Given the following data structure, return a new list with the same structure, but with the values in each sublist ordered in ascending order as strings (that is, the numbers should be treated as strings). Use a comprehension if you can. (Try using a for loop first.)


# inner_reversed_lst = []

# for inner_lst in lst:
#     inner_reversed_lst.append(sorted(inner_lst, key=str))

inner_reversed_lst = [sorted(l, key=str) for l in lst]


print(inner_reversed_lst) # [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]

