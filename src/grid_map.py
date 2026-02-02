import numpy as np

class GridMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width))  # Initialize a grid with 0s (empty spaces)

    def add_obstacle(self, x, y):
        """Adds an obstacle if the coordinates are within bounds and not already an obstacle."""
        if self.is_within_bounds(x, y):
            if self.grid[y, x] == 1:
                raise ValueError("Obstacle already exists at this location")
            self.grid[y, x] = 1  # Mark the cell as an obstacle
        else:
            raise ValueError("Obstacle coordinates out of bounds")

    def remove_obstacle(self, x, y):
        """Removes an obstacle if the coordinates are within bounds and currently an obstacle."""
        if self.is_within_bounds(x, y):
            if self.grid[y, x] == 0:
                raise ValueError("No obstacle found at this location to remove")
            self.grid[y, x] = 0  # Clear the obstacle
        else:
            raise ValueError("Coordinates out of bounds")

    def is_within_bounds(self, x, y):
        """Checks if the provided coordinates are within the grid boundaries."""
        return 0 <= x < self.width and 0 <= y < self.height

    def display(self):
        """Prints the current state of the grid map."""
        print(self.grid)
    
    def get_grid(self):
        """Returns a copy of the current grid."""
        return np.copy(self.grid)

# Example usage
if __name__ == '__main__':
    grid_map = GridMap(10, 10)  # Create a 10x10 grid
    grid_map.add_obstacle(2, 3)  # Add an obstacle at (2, 3)
    grid_map.display()  # Display the grid
    grid_map.remove_obstacle(2, 3)  # Remove an obstacle at (2, 3)
    grid_map.display()  # Display the grid again
