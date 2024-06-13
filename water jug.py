from collections import deque

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def water_jug_solver(x, y, goal_x, goal_y, initial_state=(0, 0)):
    # Check if the target volume is achievable
    if goal_x > x or goal_y > y:
        return "No solution possible: Goal state exceeds jug capacities."
    if (goal_x % gcd(x, y) != 0) or (goal_y % gcd(x, y) != 0):
        return "No solution possible: Goal state not reachable with given jug sizes."

    # Setup for BFS
    queue = deque([(initial_state[0], initial_state[1], [('Initial State', initial_state[0], initial_state[1])])])  # (current x, current y, list of steps)
    visited = set((initial_state[0], initial_state[1]))

    while queue:
        cur_x, cur_y, path = queue.popleft()

        # Check if we've reached the solution
        if cur_x == goal_x and cur_y == goal_y:
            return path + [('Goal State', cur_x, cur_y)]

        # Generate all possible states from current state
        states = [
            (x, cur_y, path + [('Fill Jug X', x, cur_y)]),  # Fill jug X completely
            (cur_x, y, path + [('Fill Jug Y', cur_x, y)]),  # Fill jug Y completely
            (0, cur_y, path + [('Empty Jug X', 0, cur_y)]),  # Empty jug X
            (cur_x, 0, path + [('Empty Jug Y', cur_x, 0)]),  # Empty jug Y
            (cur_x - min(cur_x, y - cur_y), cur_y + min(cur_x, y - cur_y), path + [('Pour X to Y', cur_x - min(cur_x, y - cur_y), cur_y + min(cur_x, y - cur_y))]),  # Pour from X to Y
            (cur_x + min(cur_y, x - cur_x), cur_y - min(cur_y, x - cur_x), path + [('Pour Y to X', cur_x + min(cur_y, x - cur_x), cur_y - min(cur_y, x - cur_x))])  # Pour from Y to X
        ]

        # Record and enqueue unvisited states
        for state in states:
            if (state[0], state[1]) not in visited:
                visited.add((state[0], state[1]))
                queue.append(state)

    return "No solution."

# Example usage - allow user input for capacities, target, initial and goal jug
x = int(input("Enter capacity for Jug X: "))
y = int(input("Enter capacity for Jug Y: "))
goal_x = int(input("Enter goal amount for Jug X: "))
goal_y = int(input("Enter goal amount for Jug Y: "))
initial_x = int(input("Enter initial amount in Jug X: "))
initial_y = int(input("Enter initial amount in Jug Y: "))

result = water_jug_solver(x, y, goal_x, goal_y, initial_state=(initial_x, initial_y))
if isinstance(result, list):
    print("Solution sequence:")
    for action, jug_x, jug_y in result:
        print(f"{action}: Jug X: {jug_x} liters, Jug Y: {jug_y} liters")
else:
    print(result)
