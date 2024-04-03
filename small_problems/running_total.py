"""
### P

input: list
output: list (presumed new list) with values transformed

explicit requirements:
    - output should have the same number of elements
    - each element after the first should reflect the running total

implicit requirements:
    - all values are integers
    - first element is the same between the two lists

questions:
    - should the list with the running totals be a new list or a mutation of the original list?
    - are all values numeric?
    - can there be negative numbers?

### E

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

- list may be empty; if empty list, stay empty list
- if there is only 1 element, new list will look the same

### D

- lists


### A

create a result list
create a running total as 0

return empty result list if input list is empty

loop through input list:
    running total += current value 
    append running total to result list

return result list


### C

see below

"""


def running_total(numbers):
    results = []
    running_total = 0

    for number in numbers:
        running_total += number
        results.append(running_total)

    return results


print(running_total([2, 5, 13]) == [2, 7, 20])  # True
print(running_total([14, 11, 7, 15, 20]) == [14, 25, 32, 47, 67])  # True
print(running_total([3]) == [3])  # True
print(running_total([]) == [])  # True
