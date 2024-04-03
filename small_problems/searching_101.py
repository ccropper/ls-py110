num1 = input("Enter the 1st number: ")
num2 = input("Enter the 2nd number: ")
num3 = input("Enter the 3rd number: ")
num4 = input("Enter the 4th number: ")
num5 = input("Enter the 5th number: ")
num6 = input("Enter the last number: ")

numbers = [num1, num2, num3, num4, num5]
numbers_str = ",".join(numbers)

if num6 in numbers:
    print(f"{num6} is in {numbers_str}.")
else:
    print(f"{num6} isn't in {numbers_str}.")
