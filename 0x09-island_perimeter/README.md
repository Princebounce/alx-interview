# Island Perimeter

This project contains a Python function island_perimeter(grid) that calculates and returns the perimeter of an island described in a given grid.

## Function Description
The island_perimeter(grid) function takes in the following parameter:

grid: A list of lists of integers representing the island.
The function returns an integer value representing the perimeter of the island.

## 
Assumptions and Constraints
- The grid is a rectangular shape, with its width and height not exceeding 100.
- Each cell in the grid is square, with a side length of 1.
- The grid is completely surrounded by water.
- The grid contains only two types of cells:
- 0 represents water.
- 1 represents land.
- Cells are connected horizontally or vertically but not diagonally.
- There is only one island in the grid, or there might be no island present.
- The island doesn't have any "lakes," meaning there is no water inside the island that isn't connected to the water surrounding the island.


### Example Usage
```

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))

```

Output:

```
12
```

## Implementation Details

The island_perimeter(grid) function calculates the perimeter of the island by iterating through each cell in the grid. It checks each land cell and counts the number of adjacent water cells. The total count of adjacent water cells gives the contribution to the perimeter from that land cell. The final sum of contributions from all land cells gives the total perimeter of the island.

The function implements the following steps:

Initialize a variable perimeter to 0.
Iterate over each row i in the grid.
Iterate over each cell j in the current row.
If the current cell is land (grid[i][j] equals 1), calculate its contribution to the perimeter by counting the adjacent water cells.
If the cell to the left (grid[i][j-1]) is water or outside the grid boundaries, increment the perimeter variable.
If the cell to the right (grid[i][j+1]) is water or outside the grid boundaries, increment the perimeter variable.
If the cell above (grid[i-1][j]) is water or outside the grid boundaries, increment the perimeter variable.
If the cell below (grid[i+1][j]) is water or outside the grid boundaries, increment the perimeter variable.
Return the perimeter variable as the final result.
Note: The implementation assumes that the input grid is valid and follows the given assumptions and constraints.


Author: Taofik Lawal
