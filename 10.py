import heapq

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)

    def __lt__(self, other):
        return self.f < other.f

def astar(grid, start, end):
    open_list = []
    closed_list = set()

    start_node = Node(None, start)
    end_node = Node(None, end)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node)

        if current_node == end_node:
            path = []
            path_cost = current_node.g
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1], path_cost

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in neighbors:
            new_position = (current_node.position[0] + dx, current_node.position[1] + dy)

            if (new_position[0] < 0 or new_position[0] >= len(grid) or 
                new_position[1] < 0 or new_position[1] >= len(grid[0])):
                continue

            if grid[new_position[0]][new_position[1]] == 1:
                continue

            new_node = Node(current_node, new_position)

            if new_node in closed_list:
                continue

            new_node.g = current_node.g + 1
            new_node.h = abs(new_position[0] - end_node.position[0]) + abs(new_position[1] - end_node.position[1])
            new_node.f = new_node.g + new_node.h

            for node in open_list:
                if new_node == node and new_node.g > node.g:
                    break
            else:
                heapq.heappush(open_list, new_node)

    return None, None

# Function to take input for the grid
def input_grid():
    grid = []
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print("Enter the grid (0 for traversable, 1 for obstacle):")
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print("Invalid input. Please enter exactly", cols, "columns.")
            return None
        grid.append(row)
    return grid

# Function to take input for start and end points
def input_start_end():
    start = tuple(map(int, input("Enter start point coordinates (row column): ").split()))
    end = tuple(map(int, input("Enter end point coordinates (row column): ").split()))
    return start, end

# Example usage:
print("Enter grid details:")
grid = input_grid()
if grid is None:
    exit()

start, end = input_start_end()

path, path_cost = astar(grid, start, end)
if path:
    print("Shortest path found:", path)
    print("Path cost:", path_cost)
else:
    print("No path found.")
