grid = [
    ['A', '0', '#'],
    ['0', '0', '#'],
    ['#', '0', 'G']
]

position = [0, 0]
visited = []

while True:
    r, c = position

    print("Position:", position)

    if grid[r][c] == 'G':
        print("Goal Reached!")
        break

    visited.append(position.copy())
    grid[r][c] = 'V'

    # Right
    if c + 1 < 3 and grid[r][c+1] in ['0', 'G']:
        position = [r, c+1]

    # Down
    elif r + 1 < 3 and grid[r+1][c] in ['0', 'G']:
        position = [r+1, c]

    # Left
    elif c - 1 >= 0 and grid[r][c-1] in ['0', 'G']:
        position = [r, c-1]

    # Up
    elif r - 1 >= 0 and grid[r-1][c] in ['0', 'G']:
        position = [r-1, c]

    else:
        print("Goal Not Found!")
        break

print("Visited:", visited)