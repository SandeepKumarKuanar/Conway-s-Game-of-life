import numpy as np 

world = np.zeros((5, 5))
required_generation = 5
"""
At each generation in time, the following transitions occur:

1. Any live cell with <2 live neighbours dies, as if caused by underpopulation.
2. Any live cell with >3 live neighbours dies, as if by overpopulation.
3. Any live cell with 2 to 3 live neighbours lives on to the next generation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by  reproduction.
"""
### we replace by arr[row, column] = [1] or [0]
## → this is the one which make generations
## stopping conditions are if np.sum(_array_) = 0 or the required generations are reached
# while required_generation > 0:
#     print(f"this is the {required_generation}\n", world)
#     required_generation -= 1
# arr = np.array([[0, 0, 0, 1, 0],
#                 [0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0]])
arr = np.array([[1, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]])
# arr = np.array([[0, 1, 0],
#                 [0, 0, 0],
#                 [0, 0, 0]])
# arr = np.array([[0, 0],
#                 [1, 0]])
## find who are alive
row, column = np.where(arr == 1)  ## where finds the closest row with the target value and then finds the column of it
print(arr)

print(row, column)
