# Can you implement a double_numbers function that mutates its argument?

numbers = [1, 4, 3, 7, 2, 6]


def double_numbers(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2
    return numbers


print(double_numbers(numbers))  # [2, 8, 6, 14, 4, 12]
print(numbers)  # [2, 8, 6, 14, 4, 12]
