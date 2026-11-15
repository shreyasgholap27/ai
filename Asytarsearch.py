import heapq

# Goal State
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Manhattan Distance
def heuristic(state):

    distance = 0

    for i in range(9):

        # 0 is blank, so ignore it
        if state[i] != 0:

            # Find goal position
            goal_index = GOAL.index(state[i])

            # Current row and column
            row1 = i // 3
            col1 = i % 3

            # Goal row and column
            row2 = goal_index // 3
            col2 = goal_index % 3

            # Manhattan Distance
            distance += abs(row1 - row2) + abs(col1 - col2)

    return distance


# Print Puzzle
def print_puzzle(state):

    for i in range(0, 9, 3):

        print(state[i:i+3])

    print()


# Generate Possible Moves
def get_neighbors(state):

    neighbors = []

    # Find blank position
    blank = state.index(0)

    # Find blank row and column
    row = blank // 3
    col = blank % 3

    # Possible moves
    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    # Try every move
    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        # Check boundary
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            # Convert row-column into index
            new_blank = new_row * 3 + new_col

            # Convert tuple into list
            new_state = list(state)

            # Swap blank and tile
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            # Convert list back to tuple
            neighbors.append(tuple(new_state))

    return neighbors


# A* Algorithm
def a_star(start):

    # Priority Queue
    priority_queue = []

    # Cost from start
    g = 0

    # Heuristic cost
    h = heuristic(start)

    # Total cost
    f = g + h

    # Insert starting state
    heapq.heappush(
        priority_queue,
        (f, g, start, [start])
    )

    # Visited states
    visited = set()

    # Continue until queue becomes empty
    while priority_queue:

        # Get state with lowest f value
        f, g, current, path = heapq.heappop(
            priority_queue
        )

        # Check goal
        if current == GOAL:

            return path

        # If already visited, skip
        if current in visited:

            continue

        # Mark as visited
        visited.add(current)

        # Generate neighbors
        for neighbor in get_neighbors(current):

            # Check if neighbor is not visited
            if neighbor not in visited:

                # New actual cost
                new_g = g + 1

                # New heuristic cost
                new_h = heuristic(neighbor)

                # New total cost
                new_f = new_g + new_h

                # Add neighbor to path
                new_path = path + [neighbor]

                # Add to priority queue
                heapq.heappush(
                    priority_queue,
                    (
                        new_f,
                        new_g,
                        neighbor,
                        new_path
                    )
                )

    # No solution
    return None


# =========================
# Main Program
# =========================

print("A* Algorithm for 8 Puzzle")
print("-------------------------")

print("Enter the puzzle row by row.")
print("Use 0 for blank space.")

# Store input
start = []

# Take 3 rows
for i in range(3):

    row = list(
        map(
            int,
            input("Enter row: ").split()
        )
    )

    start.extend(row)


# Convert list into tuple
start = tuple(start)


# Display initial state
print("\nInitial State:")
print_puzzle(start)


# Run A* Algorithm
solution = a_star(start)


# Display result
if solution:

    print("Solution found!")

    print(
        "Number of moves:",
        len(solution) - 1
    )

    print("\nSteps:")

    # Print every step
    for step, state in enumerate(solution):

        print("Step", step)

        print_puzzle(state)

else:

    print("No solution found.")