import random

# define size of the maze
size = 20

# initialize maze with walls
maze = [[1 for i in range(size+2)] for j in range(size+2)]

# carve out the maze using depth-first search algorithm
def dfs(x, y):
    maze[x][y] = 0

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x+2*dx, y+2*dy
        if nx < 1 or nx > size or ny < 1 or ny > size:
            continue
        if maze[nx][ny] == 1:
            maze[x+dx][y+dy] = 0
            dfs(nx, ny)

# carve out the maze starting from the center
dfs(size//2, size//2)

# print the maze
for row in maze:
    # add comma to each row
    print(row, end=',\n')
