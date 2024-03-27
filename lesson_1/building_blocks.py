"""
Leftover Blocks

P - PROBLEM: 

Write a program that, given the number of available blocks, calculates the number of blocks left over after building the tallest possible valid structure.

Inputs:
    - a integer representing the number of available blocks

Outputs:
    - an integer representing the number of blocks left over after completing the last complete layer

Explicit requirements:
    - the building blocks are cubes
    - the structure is built in layers
    - the top layer is a single block
    - a block in an upper layer must be supported by four blocks in a lower layer
    - a block in a lower layer can support more than one block in an upper layer
    - you cannot leave gaps between the blocks

Implicit requirements:
    - the input has to be positive
    - the output has to be positive
    - examples of valid (complete) layers:

        top layer:      [ ] 

        second layer:   [ ] [ ]
                        [ ] [ ]

        third layer:    [ ] [ ] [ ]
                        [ ] [ ] [ ]
                        [ ] [ ] [ ]

        fourth layer:   [ ] [ ] [ ] [ ]
                        [ ] [ ] [ ] [ ]
                        [ ] [ ] [ ] [ ]
                        [ ] [ ] [ ] [ ]

    - the relationship follows this pattern: 1, 4, 9, 16... which represents the square of the layer number

Clarifying questions:
- is there a maximum height for the structure after a certain number of layers? 
- what happens if there are zero blocks provided? 
- (missed) what happens if there are no leftover blocks?
- (missed) can a layer have more blocks than are strictly needed for supporting the block(s) above?

E - EXAMPLES & TEST CASES

test cases:

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True

these test cases help answer some questions:
    - if provided 0 blocks, there are 0 blocks left 
    - there can be 0 blocks left after building complete layer(s)
    - (missed) layers can only have as many blocks are are strictly needed to support the blocks above to be valid
    - we will need to have a running sum of the total blocks used to build complete layers to determine the leftover blocks
    - the leftover blocks are the difference between the total blocks and the last complete layer

D - DATA STRUCTURES:

Data structures needed:
    - we can use a dictionary to store the number of blocks that belong with each layer
    - alternately, we could use a list whereby the index (offset by 1) can represent the layer number


A - ALGORITHM:

1. Take an input that represents the total number of blocks available
2. find the sum of blocks in layers that add up the a number less than the total number of blocks availble
    - check if blocks available is 0 and return 0 if 0
    - initialize a variable to keep track of layer number
    - initialize a variable to keep track of sum of blocks used
    - initialize a variable to keep track of sum of blocks still available
    - WHILE sum of blocks used in complete layers is fewer than available blocks
        - use the layer number to calculate the number of blocks in next layer
        - if blocks in layer is less than available blocks:
            - break out of loop
        - add the blocks used to blocks used variable
        - subtract the blocks in layer from available blocks
        - increment the layer number
        
3. return the difference as the output

C - CODE:

See below
"""


def calculate_leftover_blocks(blocks):
    if blocks == 0:
        return 0

    layer = 1
    blocks_used = 0
    blocks_available = blocks

    while blocks_used < blocks:
        blocks_in_layer = layer**2
        if blocks_in_layer > blocks_available:
            break
        blocks_used += blocks_in_layer
        blocks_available -= blocks_in_layer
        layer += 1

    return blocks_available


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0)  # True
