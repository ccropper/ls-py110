# Given the following data structure, write some code to return a list that contains the colors of the fruits and the sizes of the vegetables. The sizes should be uppercase, and the colors should be capitalized.

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def get_produce_property(produce):
        if produce['type'] == 'fruit':
            return [color.capitalize() for color in produce['colors']]
        if produce['type'] == 'vegetable':
            return produce['size'].upper()

new_list = [(get_produce_property(produce)) for produce in dict1.values()]

print(new_list) # [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]