import sys
import heapq

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.target = 'g'
        self.rows = len(maze)
        self.cols = len(maze[0])
    
    def printMaze(self):
        for row in self.maze:
            print(''.join(row))
        print()
    
    def shortestPath(self, start):
        # Initialize distances with infinity
        distances = {(i, j): float('inf') for i in range(self.rows) for j in range(self.cols)}
        distances[start] = 0
        prev = {}
        
        # Priority queue to store cells to visit, prioritized by distance
        queue = [(0, start)]
        heapq.heapify(queue)
        
        while queue:
            dist, node = heapq.heappop(queue)
            x, y = node
            
            # Check if goal is reached
            if self.maze[x][y] == self.target:
                # Backtrack to find the path
                path = []
                while node in prev:
                    path.append(node)
                    node = prev[node]
                path.append(start)
                path.reverse()
                return dist, path
            
            # Check adjacent cells
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.rows and 0 <= ny < self.cols and self.maze[nx][ny] != '#':
                    new_dist = dist + 1
                    if new_dist < distances[(nx, ny)]:
                        distances[(nx, ny)] = new_dist
                        prev[(nx, ny)] = (x, y)
                        heapq.heappush(queue, (new_dist, (nx, ny)))
        
        return float('inf'), []

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Use: filename.py x y")
        sys.exit(1)
    
    start_x = int(sys.argv[1])
    start_y = int(sys.argv[2])
    
    maze = [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', ' ', ' ', ' ', ' ', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', ' ', '#', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', ' ', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', 'g', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]
    
    solver = MazeSolver(maze)
    shortest_dist, shortest_path = solver.shortestPath((start_x, start_y))
    if shortest_dist != float('inf'):
        print(f"Shortest path to goal with distance {shortest_dist}:")
        for cell in shortest_path:
            print(cell)
    else:
        print("No path to the goal found.")

