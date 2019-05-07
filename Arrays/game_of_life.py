def get_next_state(grid):
    new_grid = []
    row_num = len(grid)
    col_num = len(grid[0])
    for i in range(row_num):
        for j in range(col_num):
            num_alive_neighbors = get_alive_neighbors(grid, i, j, row_num, col_num)
            # Alive
            if grid[i][j] == 1:
                if (num_alive_neighbors != 2 and num_alive_neighbors != 3):
                    new_grid[i][j] = 0

            # Dead
            if grid[i][j] == 0:
                if(num_alive_neighbors == 3):
                    new_grid[i][j] = 1
    return new_grid


def get_alive_neighbors(grid, i, j, num_rows, num_cols):
    res = 0
    for x in [-1,0,1]:
        for y in [-1,0,1]:
                if x == 0 and y == 0:
                    continue
                res = res + get_grid_value(grid, i+x, j+y, num_rows, num_cols)
    return res

def get_grid_value(grid, i, j, num_rows, num_cols):
    if i < 0 or i >= num_rows or j < 0 or j >= num_cols:
        return 0
    return grid[i][j]
    
def main():
    a = [[1,0,1],[1,0,1],[1,0,1]]
    print(get_next_state(a))

main()




"""
    •    If the cell is alive: if it has 2 or 3 alive neighbors, it stays alive. Otherwise, it dies.
    •    If the cell is dead: if it has exactly 3 alive neighbors, it becomes alive. Otherwise, it stays dead.
    •    The state of each cell is determined only by the state of its neighbors in the last iteration.
"""


# ---------
# 0 | 1 | 0       0 1 0
# ---------
# 1 | 0 | 1  ->   1 0 1
# ---------
# 1 | 1 | 0       1 1 0
# ---------

before_arr = []
curr_arr = [0,1,0]
next_arr = [1,0,1]

# UPDATE curr_arr

# Updare before_arr, curr_arr, next_arr
before_arr = curr_arr
curr_arr = next_arr
next_arr = next_next



def get_next_state(grid):
    row_num = len(grid)
    col_num = len(grid[0])

    new_grid = []

    for i in row_num:
        for j in col_num:
            num_alive_neighbors = get_alive_neighbors(i, j, grid, row_num)
            # Cell is alive
            if grid[i][j] == 1:
                # If 2 or 3 alive neighbors, keep the cell alive
                if (num_alive_neighbors != 2 and num_alive_neighbors != 3):
                    new_grid[i][j] == 0
            # Cell is dead
            if grid[i][j] == 0:
                if num_alive_neighbors == 3:
                    new_grid[i][j] = 1

    return new_grid

def get_alive_neighbors(i, j, grid, len):
    # Edge Nodes
    if (i == 0 and j == 0):
        return grid[i][j+1] + grid[i+1][j+1] + grid[i+1][j]
    if (i == 0 and j == len -1):
        return grid[i][len-2] + grid[i+1][len-2] + grid[i+1][j]
    if (i == len-1 and j == len - 1):
        return grid[i][j-1] + grid[i-1][j-1] + grid[i-1][j]
    if (i == len -1 and j == 0):
        return grid[i-1][j] + grid[i-1][j+1] + grid[i][j+1]

    # Top node
    if i == 0 and (j>=1 and j <= len-1):
        return grid[i][j-1] + grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1] + grid[i][j+1]

    # Left node
    if j == 0 and (i>=1 and j <= len-2):
        return grid[i-1][j] + grid[i-1][j+1] + grid[i][j+1] + grid[i+1][j+1]+ grid[i+1][j]

    # Bottom node
    if i == len-1 and (j >= 1 and j <= len-2):
        return grid[i][j-1] + grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] + grid[i][j+1]

    # Right node
    if j == len-1 and (i >= 1 and i <= len-2):
        return grid[i-1][j] + grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j-1] + grid[i+1][j]

    # Otherwise, center node
    return grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] + grid[i][j-1] + grid[i][j+1] + grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]


# Center Node Everything else

# Edge Nodes (0,0) (len-1, len-1) (0, len-1) (len-1, 0)

# Top, Left, Bottom, Right Nodes
   # Top: (0, 1) -> (0, len-1)
   # Left: (1, 0) -> (len-2, 0)
   # Bottom: (len-1, 1) -> (len-1, len-2)
   # Right: (1, len-1) -> (len-2, len-1)

#
# Your previous Plain Text content is preserved below:
#
# Hello Ralph

# ---------
# 0 | 1 | 0       0 1 0
# ---------
# 1 | 0 | 1  ->   1 0 1
# ---------
# 1 | 1 | 0       1 1 0
# ---------
