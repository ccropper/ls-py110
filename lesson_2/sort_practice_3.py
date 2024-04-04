lst = [10, 9, -6, 11, 7, -16, 50, 8]

print(sorted(lst, key=str))

print(sorted(lst, key=str, reverse=True))


# [-16, -6, 10, 11, 50, 7, 8, 9]          # Ascending sort
# [9, 8, 7, 50, 11, 10, -6, -16]          # Descending sort
