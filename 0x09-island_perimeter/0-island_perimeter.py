#!/usr/bin/python3
"""
Calculate the perimeter of the island described in the grid.

    Args:
    - grid (list of list of integers): 2D grid where 0 represents water and 1 represents land.

    Returns:
    - int: Perimeter of the island.
"""
def island_perimeter(grid):
    """ function that outputs the perimeter of an island described by grid """

    if not grid or not grid[0]:
        return 0  # Empty grid

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Start with assuming all sides are surrounded by water

                # Check neighboring cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 if the upper neighbor is land
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 if the left neighbor is land

    return perimeter

