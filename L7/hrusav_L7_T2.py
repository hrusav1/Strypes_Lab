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
        if not (0 <= x < len(self.maze) and 0 <= y < len(self.maze[0])):
            return False
        
        if (x, y) in self.visited:
            return False
        
        if self.maze[x][y] == self.target:
            return True
        
        if self.maze[x][y] in {'#', '.', 'x'}:
            return False
        
        self.visited.add((x, y))
        self.maze[x][y] = '.'
        
        # Check adjacent cells
        if (self.solveMaze(x+1, y) or
            self.solveMaze(x-1, y) or
            self.solveMaze(x, y+1) or
            self.solveMaze(x, y-1)):
            return True
        
        # If none of the adjacent cells lead to the goal, backtrack
        self.maze[x][y] = 'x'
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
        ['#', '#', '#', '#', ' ', ' ', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', 'g', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#']
    ] 
    
    solver = MazeSolver(maze)
    if solver.solveMaze(start_x, start_y):
        print("Path found:")
        solver.printMaze()
    else:
        print("No path to the goal found.")

