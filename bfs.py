# Robot Path Planning using BFS on a 5x5 Grid
# 0 = Free cell, 1 = Obstacle

from collections import deque

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

source = (0, 0)
destination = (4, 4)

def bfs(grid, source, destination):
    rows = len(grid)
    cols = len(grid[0])
    
    queue = deque()
    queue.append((source, [source]))
    print(queue)

    visited = set()
    visited.add(source)
    print(visited)

    # Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        current, path = queue.popleft()

        print("Visiting:", current)
        print(path)

        if current == destination:
            return path

        r, c = current

        for dr, dc in directions:
            print(f'dr, dc: {dr}, {dc}')
            nr = r + dr
            nc = c + dc
            next_cell = (nr, nc)
            print(next_cell)

            if (0 <= nr < rows and
                0 <= nc < cols and
                grid[nr][nc] == 0 and
                next_cell not in visited):
        

                visited.add(next_cell)
                queue.append((next_cell, path + [next_cell]))
                print(f'queueee{queue}')
                print(nr, nc)

    return None


path = bfs(grid, source, destination)

print("\nShortest Path:")

if path:
    for cell in path:
        print(cell)
    print("\nNumber of moves:", len(path) - 1)
else:
    print("No path found")
