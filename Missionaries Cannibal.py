from collections import deque

def is_valid_state(state):
    m, c, b = state
    # Check if missionaries are outnumbered on either side of the river
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False
    return True

def get_next_states(current_state):
    moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
    next_states = []
    m, c, b = current_state
    for move in moves:
        if b == 1:  # Boat is on the original side
            new_state = (m - move[0], c - move[1], 0)
        else:       # Boat is on the other side
            new_state = (m + move[0], c + move[1], 1)
        if is_valid_state(new_state):
            next_states.append(new_state)
    return next_states

def bfs():
    initial_state = (3, 3, 1)  # (Missionaries, Cannibals, Boat)
    goal_state = (0, 0, 0)
    queue = deque([(initial_state, [initial_state])])
    visited = set()
    visited.add(initial_state)
    
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path
        
        for next_state in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
    
    return None

solution = bfs()
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution possible.")
