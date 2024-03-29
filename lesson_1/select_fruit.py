produce = {
    "apple": "Fruit",
    "carrot": "Vegetable",
    "pear": "Fruit",
    "broccoli": "Vegetable",
}


def select_fruit(produce):
    # we want to select the key-value pairs where the value is 'Fruit'.
    fruits = {}

    for produce, category in produce.items():
        if category == "Fruit":
            fruits[produce] = category

    return fruits


print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }
