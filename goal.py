# Goal Stack Planning - Blocks World
# Initial State: B is on A; A, C and D are on the table
# Goal State: C on A and B on D

goal_stack = []
plan = []
hand = None


# Goal Stack functions
def push(item):
    goal_stack.append(item)
    print("PUSH:", item)


def pop():
    item = goal_stack.pop()
    print("POP :", item)
    return item


# Blocks World operations
def hold(block):
    global hand
    hand = block
    plan.append("HOLD(" + block + ")")
    print("HOLD:", block)


def unstack(block1, block2):
    global hand
    hand = block1
    plan.append("UNSTACK(" + block1 + "," + block2 + ")")
    print("UNSTACK:", block1, "from", block2)


def putdown(block):
    global hand
    hand = None
    plan.append("PUTDOWN(" + block + ")")
    print("PUTDOWN:", block)


def stack(block1, block2):
    global hand
    hand = None
    plan.append("STACK(" + block1 + "," + block2 + ")")
    print("STACK:", block1, "on", block2)


# Display Initial State
print("INITIAL STATE")
print("""
       [ B ]

       [ A ]     [ C ]     [ D ]
-----------------------------------
""")


# Push goals onto Goal Stack
push("ON(B,D)")
push("ON(C,A)")


print("\n--- GOAL STACK PLANNING STARTED ---\n")


# Process goals using LIFO order
while goal_stack:

    goal = pop()

    # Goal: C should be on A
    if goal == "ON(C,A)":

        print("\nGoal: Place C on A")
        print("B is on A, so first clear A.")

        unstack("B", "A")
        putdown("B")
        hold("C")
        stack("C", "A")

    # Goal: B should be on D
    elif goal == "ON(B,D)":

        print("\nGoal: Place B on D")

        hold("B")
        stack("B", "D")


# Display Final Plan
print("\n--- FINAL PLAN ---")

for step in plan:
    print(step)


# Display Goal State
print("\nGOAL STATE ACHIEVED")

print("""
       [ C ]               [ B ]

       [ A ]               [ D ]
-----------------------------------
""")
