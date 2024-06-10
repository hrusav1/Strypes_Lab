import sys

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.visited = set()
        self.target = 'g'
    
    def printMaze(self):
        for row in self.maze:
            print(''.join(row))
        print()
    
    def solveMaze(self, x, y):
        stack = [((x, y), [])]  # Each stack item holds coordinates and the path taken

        while stack:
            (x, y), path = stack.pop()
            print(f"Visiting: ({x}, {y})")  # Debug print
            self.printMaze()

            if not (0 <= x < len(self.maze) and 0 <= y < len(self.maze[0])):
                print(f"Out of bounds: ({x}, {y})")  # Debug print
                continue

            if (x, y) in self.visited:
                print(f"Already visited: ({x}, {y})")  # Debug print
                if self.maze[x][y] == '.':
                    self.maze[x][y] = 'x'
                continue

            self.visited.add((x, y))

            cell_value = self.maze[x][y]
            print(f"Cell value at ({x}, {y}): {cell_value}")  # Debug print

            if cell_value == self.target:
                print(f"Goal found at ({x}, {y}). Goal reached.")  # Debug print
                self.printMaze()
                return True

            if cell_value == '#' or cell_value == 'x':
                print(f"Hit wall or revisited cell at ({x}, {y}). Backtracking...")  # Debug print
                continue

            if cell_value == ' ':
                self.maze[x][y] = '.'  # Mark the current cell as part of the path

            path.append((x, y))  # Add current cell to the path

            # Check all adjacent cells and prioritize unvisited ones
            neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            unvisited_neighbors = [pos for pos in neighbors if pos not in self.visited and 0 <= pos[0] < len(self.maze) and 0 <= pos[1] < len(self.maze[0]) and self.maze[pos[0]][pos[1]] != '#']

            if unvisited_neighbors:
                for pos in unvisited_neighbors:
                    stack.append((pos, path[:]))
            else:
                # If no unvisited neighbors, consider it a backtrack step
                for pos in neighbors:
                    stack.append((pos, path[:]))

        print("No path to the goal found.")  # Debug print
        self.printMaze()
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Use: filename.py x y")
        sys.exit(1)

    start_x = int(sys.argv[1])
    start_y = int(sys.argv[2])

    maze = [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', ' ', '#', '#', '#', ' ', '#', '#'],
        ['#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', ' ', ' ', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', 'g', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]

    solver = MazeSolver(maze)
    solver.solveMaze(start_x, start_y)

