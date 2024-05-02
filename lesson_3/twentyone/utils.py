def prompt(message):
    print(f"=> {message}")


def join_or(lst, delimiter=",", last_joining_word="or"):
    delimiter = delimiter.strip()
    joined_elements = ""
    if len(lst) == 1:
        joined_elements = lst[0]
    if len(lst) == 2:
        joined_elements = f"{lst[0]} {last_joining_word} {lst[1]}"
    if len(lst) > 2:
        for el in lst[:-1]:
            joined_elements += f"{el}{delimiter} "
        joined_elements += f"{last_joining_word} {lst[-1]}"

    return joined_elements


# print(join_or([1, 2, 3]))  # => "1, 2, or 3"
# print(join_or([1, 2, 3], "; "))  # => "1; 2; or 3"
# print(join_or([1, 2, 3], ", ", "and"))  # => "1, 2, and 3"
# print(join_or([]))  # => ""
# print(join_or([5]))  # => "5"
# print(join_or([1, 2]))  # => "1 or 2"
