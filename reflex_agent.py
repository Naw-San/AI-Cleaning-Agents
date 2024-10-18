class ReflexAgent:
    def __init__(self, environment):
        """
        Initializes the ReflexAgent with a reference to the environment and sets its starting position
        to a random (x, y) coordinate within the environment's grid.

        Parameters:
        - environment: The environment in which the agent operates, with dimensions M x N.
        """
        self.env = environment
        # Start the agent at a random position within the grid
        self.x, self.y = np.random.randint(0, self.env.M), np.random.randint(0, self.env.N)

    def act(self):
        """
        Defines the agent's actions at each time step.
        - If the current location has dirt (i.e., grid value > 0), the agent cleans the dirt by calling `suck()`.
        - The agent then moves to a new location randomly by calling the `move()` method.
        """
        # If there is dirt at the agent's current location, clean it
        if self.env.grid[self.x, self.y] > 0:
            self.suck()

        # Move to a new location after cleaning (if necessary)
        self.move()

    def move(self):
        """
        Moves the agent to a neighboring cell. The agent randomly chooses one of four directions:
        up, down, left, or right. It then updates its position, ensuring it stays within the grid boundaries.
        """
        moves = ['up', 'down', 'left', 'right']  # Possible movement directions
        move = random.choice(moves)  # Randomly choose a direction

        # Update the agent's position based on the chosen direction, ensuring it doesn't go out of bounds
        if move == 'up' and self.x > 0:
            self.x -= 1
        elif move == 'down' and self.x < self.env.M - 1:
            self.x += 1
        elif move == 'left' and self.y > 0:
            self.y -= 1
        elif move == 'right' and self.y < self.env.N - 1:
            self.y += 1

    def suck(self):
        """
        Cleans the current cell by setting its value to 0, indicating the dirt has been removed.
        """
        self.env.grid[self.x, self.y] = 0  # Set the current cell to clean
