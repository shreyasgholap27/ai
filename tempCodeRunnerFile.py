from collections import deque

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]


source = (0, 0)
destination = (4,4)



def bfs(source,destination,grid):
    rows = len(grid)
    cols = len(grid[0])
    
    queue = deque()
    queue.append((source,[source]))
    visited = set()
    visited.add(source)
    
    direction  = [(-1,0),(1,0),(0,-1),(0,1)]
    


    while queue:
        current, path = queue.popleft()
        
        if current == destination:
            return path
        
        r,c = current
        for dr,dc in direction:
            nr = r+dr
            nc = c+dc
            next_cell = (nr,nc)
            
            if (0<=nr<rows and
                0<=nc<cols and
                grid[nr][nc]==0 and
                next_cell not in visited):
                    
                    visited.add(next_cell)
                    queue.append((next_cell,path+[next_cell]))
                    
    return 0

path = bfs(source,destination,grid)
if path:
    for cell in path:
        print(cell)
    print("\nNumber of moves:", len(path) - 1)
else:
    print("No path found")