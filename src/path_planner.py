import heapq

class PathPlanner:
    def __init__(self, grid):
        self.grid = grid  # The grid map representation of the environment
        self.width = len(grid[0]) if grid else 0
        self.height = len(grid)

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

    def astar(self, start, goal):
        if not self.is_within_bounds(start) or not self.is_within_bounds(goal):
            print("Start or goal point is out of bounds.")
            return []

        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}

        g_score = {node: float('inf') for y in range(self.height) for x in range(self.width)}
        g_score[start] = 0

        f_score = {node: float('inf') for y in range(self.height) for x in range(self.width)}
        f_score[start] = self.heuristic(start, goal)

        while open_set:
            current = heapq.heappop(open_set)[1]

            if current == goal:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + 1  # Assume cost from current to neighbor is 1
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + self.heuristic(neighbor, goal)

                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

        print("No path found from start to goal.")
        return []  # Return an empty path if no path is found

    def reconstruct_path(self, came_from, current):
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        return total_path[::-1]  # Return reversed path

    def get_neighbors(self, node):
        x, y = node
        neighbors = []

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Left, right, down, up
            neighbor = (x + dx, y + dy)
            if self.is_within_bounds(neighbor):
                if self.grid[neighbor[0]][neighbor[1]] == 0:  # Assuming 0 is walkable
                    neighbors.append(neighbor)

        return neighbors

    def is_within_bounds(self, node):
        x, y = node
        return 0 <= x < self.height and 0 <= y < self.width

    def add_obstacle(self, position):
        if self.is_within_bounds(position):
            x, y = position
            self.grid[x][y] = 1  # Assuming 1 represents an obstacle

    def remove_obstacle(self, position):
        if self.is_within_bounds(position):
            x, y = position
            self.grid[x][y] = 0  # Reset to walkable space
