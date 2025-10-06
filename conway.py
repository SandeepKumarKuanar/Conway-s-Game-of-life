import numpy as np

world = np.zeros((5, 5))
"""
At each generation in time, the following transitions occur:
1. Any live cell with <2 live neighbours dies, as if caused by underpopulation.
2. Any live cell with >3 live neighbours dies, as if by overpopulation.
3. Any live cell with 2 to 3 live neighbours lives on to the next generation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""
### we replace by arr[row, column] = [1] or [0]
## → this is the one which make generations
## stopping conditions are if np.sum(_array_) = 0 or the required generations are reached
# world = np.array([
#     [0, 1, 0, 0, 0], 
#     [1, 1, 0, 0, 0], 
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0]
# ])
# world = np.array([
#     [0, 1, 0, 0], 
#     [1, 1, 0, 0], 
#     [0, 0, 0, 0],
#     [0, 0, 0, 0]
# ])
# world = np.array([
#     [0, 1, 0], 
#     [1, 1, 0], 
#     [0, 0, 0]
# ])
# world = np.array([
#     [0, 1], 
#     [1, 1]
# ])
### testing the glider. . .
# world = np.array([
#     [0, 1, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0],
#     [1, 1, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0]
# ])

world = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])
###### functions to access every element in the world
#### corners ----- 
def top_left(arr, row, column):
    return arr[:row+2, :column+2]

def top_right(arr, row, column):
    return arr[:row+2, column-1:]

def low_left(arr, row, column):
    return arr[row-1:, :column+2]

def low_right(arr, row, column):
    return arr[row-1:, column-1:]
#### -----
def first_row(arr, row, column):
    return arr[:row+2, column-1 : column+2]

def first_column(arr, row, column):
    return arr[row-1:row+2, :column+2]

def last_row(arr, row, column):
    return arr[row-1:, column-1:column+2]

def last_column(arr, row, column):
    return arr[row-1:row+2, column-1:]

#### ---- rest of the cases
def rest(arr, row, column):
    return arr[row-1:row+2, column-1:column+2]

### say for an m*m matrix world 
# we get inconveniences at
## 1. row = 0 and column = 0
## 2. row = 0 and column = m-1
## 3. row = m-1 and column = 0
## 4. row = 0 and column = any
## 5. row = any and column = 0
# tackling them below
#### accessing the world
def access_the_world(row, column, arr):
    # GROUP 1: Handling all four corners first.
    if row == 0 and column == 0:
        return top_left(arr, row, column)
    elif row == 0 and column == columns - 1:
        return top_right(arr, row, column)
    elif row == rows - 1 and column == 0:
        return low_left(arr, row, column)
    elif row == rows - 1 and column == columns - 1:
        # You'll need to define low_right based on your earlier logic
        return low_right(arr, row, column)

    # GROUP 2: Now that corners are handled.
    elif row == 0:
        return first_row(arr, row, column)
    elif row == rows - 1:
        return last_row(arr, row, column)
    elif column == 0:
        return first_column(arr, row, column)
    elif column == columns - 1:
        # You'll need to define last_column
        return last_column(arr, row, column)

    else:
        return rest(arr, row, column)

#### now using the above algorithm, we would decide the fate of the element of the world 
#### using the Conway's rules 
def fate(row, column, world, copy_arr):
    micro_environment = access_the_world(row, column, world)
    ## in the np.sum() function, it adds the in-focus cell as well, 
    ## so for 1, the sum is off by +1, so we subtract it 
    if world[row, column] == 1:
        sum_of_micro_environment = np.sum(micro_environment) - 1
        if sum_of_micro_environment < 2:
            copy_arr[row, column] = 0

        elif sum_of_micro_environment > 3:
            copy_arr[row, column] = 0

        else:
            copy_arr[row, column] = 1

    ## and for 0, the sum is the same, so we don't tamper it at all
    else:
        sum_of_micro_environment = np.sum(micro_environment)
        if sum_of_micro_environment == 3:
            copy_arr[row, column] = 1

matrix = np.shape(world) ## ← comes in tuple
rows, columns = matrix[0], matrix[1]
## printing like would print them row-wise
print("Below is the original world")
print(world) 
print()
required_generation = 4
current_generation = 1
while current_generation < required_generation + 1:
    ### the real world shouldn't change, so we make a copy of te world here, 
    print(f"This is the current generation = {current_generation}")
    copy_arr = np.copy(world)
    ## as we move further down the code, we would like to apply the rules of Conway on the copied world, and not the real world 
    for row in range(0, rows):
        for column in range(0, columns):
            fate(row, column, world, copy_arr)

    print(copy_arr, "\n")
    print("This would stay only 5 seconds")
    ## after 1 generation, now I am reassigning the copy to the main, and now we would perform our operations on the updated world
    world = copy_arr
    current_generation += 1