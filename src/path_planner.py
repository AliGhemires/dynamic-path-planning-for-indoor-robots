import numpy as np
from collections import deque

class PathPlanner:
    def __init__(self, grid):
        """
        Initialize the PathPlanner with a grid representation of the environment.
        :param grid: 2D array with 0 indicating free space and 1 indicating occupied space.
        """
        self.grid = grid  # 2D array representing occupancy (0: free, 1: occupied)
        self.rows, self.cols = grid.shape

    def heuristic(self, a, b):
        """
        Calculate the Manhattan distance heuristic from point a to point b.
        :param a: tuple representing the (x, y) coordinates of the starting position.
        :param b: tuple representing the (x, y) coordinates of the goal position.
        :return: Integer representing the estimated cost from a to b.
        """
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

    def a_star(self, start, goal):
        """
        Perform A* pathfinding algorithm.
        :param start: tuple representing the (x, y) coordinates of the start node.
        :param goal: tuple representing the (x, y) coordinates of the goal node.
        :return: List of nodes (tuples) representing the path from start to goal.
        """
        if not self._is_within_bounds(start) or not self._is_within_bounds(goal):
            return []  # Start or goal out of bounds

        open_set = set()
        open_set.add(start)
        came_from = {}

        g_score = {node: float('inf') for node in np.ndindex(self.grid.shape)}
        g_score[start] = 0

        f_score = {node: float('inf') for node in np.ndindex(self.grid.shape)}
        f_score[start] = self.heuristic(start, goal)

        while open_set:
            current = min(open_set, key=lambda node: f_score[node])
            if current == goal:
                return self.reconstruct_path(came_from, current)

            open_set.remove(current)
            neighbors = self.get_neighbors(current)
            for neighbor in neighbors:
                if not self._is_free(neighbor):
                    continue  # Skip if the neighbor is an obstacle
                tentative_g_score = g_score[current] + 1  # All edges have same weight
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + self.heuristic(neighbor, goal)
                    if neighbor not in open_set:
                        open_set.add(neighbor)

        return []  # Path not found

    def get_neighbors(self, node):
        """
        Retrieve the neighboring nodes for a given node.
        :param node: tuple representing the (x, y) coordinates of the current node.
        :return: List of tuples representing valid neighboring coordinates.
        """
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        for d in directions:
            new_node = (node[0] + d[0], node[1] + d[1])
            if self._is_within_bounds(new_node) and self._is_free(new_node):
                neighbors.append(new_node)
        return neighbors

    def reconstruct_path(self, came_from, current):
        """
        Reconstructs the path from start to goal using the came_from map.
        :param came_from: Dictionary mapping current node to its predecessor.
        :param current: tuple representing the end node from which path should be reconstructed.
        :return: List of tuples representing the path from start to current node.
        """
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        return total_path[::-1]  # Reverse the path

    def add_obstacle(self, obstacle):
        if self._is_within_bounds(obstacle):
            self.grid[obstacle[0]][obstacle[1]] = 1  # Mark as occupied

    def remove_obstacle(self, obstacle):
        if self._is_within_bounds(obstacle):
            self.grid[obstacle[0]][obstacle[1]] = 0  # Mark as free

    def _is_within_bounds(self, node):
        return 0 <= node[0] < self.rows and 0 <= node[1] < self.cols

    def _is_free(self, node):
        return self.grid[node[0]][node[1]] == 0
