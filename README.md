## Tagline
An intelligent planner for autonomous indoor navigation.

## Project Overview

## Features
- **Dynamic Path Adjustment**: Automatically recalibrates routes when encountering new obstacles, ensuring efficient navigation.
- **Real-Time Visualization**: Continuously displays the planned path for monitoring and evaluation.
- **User-Defined Points**: Allows users to specify custom start and goal locations for flexibility.

## Key Concepts
- **Dynamic Path Planning**: Modify routes dynamically as the environment changes and new obstacles are detected.
- **Grid-Based Mapping**: Uses a grid layout to efficiently represent the navigation environment, simplifying pathfinding logic.

## Main Algorithm
The project utilizes an enhanced A* pathfinding algorithm integrated with dynamic obstacle detection and avoidance, ensuring reliable route planning in fluctuating scenarios.

## Installation and Running
To set up and run the project, follow these steps:

1. **Clone the Repository:**
 ```bash
 git clone https://github.com/your-username/DynamicPathPlanning.git
 cd DynamicPathPlanning
 ```

2. **Install Necessary Libraries:**
 - Make sure you have any required dependencies installed.
 ```bash
 pip install -r requirements.txt # Only if there are dependencies specified
 ```

3. **Execute the Path Planning Program:** Run the following commands to test different functionalities:
 ```bash
 python src/main.py --start 0 0 --goal 5 5
 python src/main.py --add_obstacle 2 3
 python src/main.py --show_path
 ```

## Example Usage
Here's an example interaction using the command-line interface:
```bash
$ python src/main.py --start 0 0 --goal 5 5
Path planned from (0, 0) to (5, 5)

$ python src/main.py --add_obstacle 2 3
Obstacle added at (2, 3)

$ python src/main.py --show_path
Current path: [(0, 0), (1, 1), (1, 2), (2, 2), (3, 3), (4, 4), (5, 5)]
```

## Testing
To confirm the accuracy and robustness of the implementation, execute the included test suite with:
```bash
pytest tests
```
This command will perform unit and integration tests, including edge-case analyses, to validate the system’s reliability.

## Repository Layout
The following directory structure organizes the project files:
```plaintext
DynamicPathPlanning/
├── README.md
├── src/
│ ├── grid_map.py
│ ├── main.py
│ ├── obstacle_manager.py
│ └── path_planner.py
└── tests/
 ├── test_obstacle_manager.py
 └── test_path_planner.py
```

## Notes
Enhancements, such as a graphical user interface (GUI), can be developed for improved user interaction and visualization capabilities.

## Conclusion
