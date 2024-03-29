def multiply(numbers, multiplier):
    return [multiplier * number for number in numbers]


my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]
