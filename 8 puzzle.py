from collections import deque

class PuzzleState:
    def __init__(self, board, moves=0, prev=None):
        self.board = board
        self.moves = moves
        self.prev = prev

    def is_goal(self, goal):
        return self.board == goal

    def get_neighbors(self):
        neighbors = []
        # Find the blank space (0)
        i, j = next((i, j) for i, row in enumerate(self.board) for j, val in enumerate(row) if val == 0)
        # Possible moves (up, down, left, right)
        directions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for di, dj in directions:
            if 0 <= di < 3 and 0 <= dj < 3:
                # Swap the blank space with a neighboring element
                new_board = [row[:] for row in self.board]
                new_board[i][j], new_board[di][dj] = new_board[di][dj], new_board[i][j]
                # Append the new state to neighbors
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))
        return neighbors

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.board])

def solve_puzzle(start, goal):
    open_set = deque([PuzzleState(start)])
    closed_set = set()

    while open_set:
        current = open_set.popleft()

        if current.is_goal(goal):
            return current

        closed_set.add(str(current.board))

        for neighbor in current.get_neighbors():
            if str(neighbor.board) not in closed_set:
                open_set.append(neighbor)

    return None

def print_solution(solution):
    path = []
    current = solution
    while current:
        path.append(current)
        current = current.prev
    path.reverse()

    print("Path to solution:")
    for step in path:
        print(f"Step {step.moves}:")
        print(step)
        print()

def input_board(prompt):
    print(prompt)
    while True:
        try:
            numbers = list(map(int, input("Enter 9 numbers (0-8) with space separation: ").split()))
            if len(numbers) == 9 and set(numbers) == set(range(9)):
                return [numbers[:3], numbers[3:6], numbers[6:9]]
            else:
                print("Invalid input. Please enter exactly 9 distinct numbers (0-8).")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def main():
    start = input_board("Enter the start configuration:")
    goal = input_board("Enter the goal configuration:")
    
    solution = solve_puzzle(start, goal)
    if solution:
        print_solution(solution)
        print("Total moves:", solution.moves)
    else:
        print("No solution found.")

# The main function is not called here.
