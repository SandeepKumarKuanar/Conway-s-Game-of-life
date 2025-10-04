# ---------
#### if they appear at the corners
## if the point is at left-topmost
# print(arr[:row[0]+2:, :column[0]+2:])

## if the point is at left-lowermost 
# print(arr[row[0]-1::, :column[0]+2:])

## if the point is at right-topmost
# print(arr[:row[0]+2:, column[0]-1::])

## if the point is at right-lowermost 
# print(arr[row[0]-1::, column[0]-1::])
# ---------

# ---------
#### fixated to the column
## fixed to the first column, but not at the corner
# print(arr[row[0]-1:row[0]+2, :column[0]+2])

## fixed to the last column, but not at the corner
# print(arr[row[0]-1:row[0]+2, column[0]-1:column[0]+2])

#### fixated to a row
## if it's in the first row, but not at the corners
# print(arr[:row[0]+2, column[0]-1:column[0]+2])

## if it's in the last row, but not at the corners
# print(arr[row[0]-1:, column[0]-1:column[0]+2])
# ---------

# ---------
#### rest all of the cases
# print(arr[row[0]-1:row[0]+2, column[0]-1:column[0]+2])