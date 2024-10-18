class Environment:
    def __init__(self, M, N, dirt_percentage):
        """
        Initializes the environment with a grid of size M x N and populates it with dirt based on the
        specified dirt percentage.

        Parameters:
        - M: Number of rows in the grid.
        - N: Number of columns in the grid.
        - dirt_percentage: Percentage of cells that should contain dirt (values > 0).
        """
        self.M = M
        self.N = N
        self.grid = np.zeros((M, N))  # Create an MxN grid initialized to 0 (clean cells)
        self.dirt_percentage = dirt_percentage
        self.initialize_dirt()  # Place dirt in the grid

    def initialize_dirt(self):
        """
        Populates the grid with dirt in a random set of cells based on the dirt percentage.
        Each dirty cell gets a random amount of dirt between 1 and 4.
        """
        total_cells = self.M * self.N  # Total number of cells in the grid
        dirt_cells = int(self.dirt_percentage * total_cells)  # Number of cells that should have dirt

        for _ in range(dirt_cells):
            x, y = np.random.randint(0, self.M), np.random.randint(0, self.N)  # Select random cell coordinates
            self.grid[x, y] += np.random.randint(1, 5)  # Assign a random amount of dirt (1 to 4)

    def print_grid(self):
        """
        Prints the grid to the console, displaying the dirt levels in each cell.
        """
        print(self.grid)

    def visualize_grid(self):
        """
        Displays a graphical representation of the grid using a heatmap, where higher dirt levels
        are represented by warmer colors (e.g., red, yellow). A color bar indicates dirt levels.
        """
        plt.imshow(self.grid, cmap='inferno', interpolation='nearest')  # Display grid using heatmap
        plt.colorbar()  # Add a color bar to show dirt levels
        plt.show()

    def get_clean_cell_percentage(self):
        """
        Calculates and returns the percentage of clean cells (cells with a dirt level of 0).

        Returns:
        - Percentage of cells that are clean.
        """
        return np.sum(self.grid == 0) / (self.M * self.N) * 100  # Percentage of clean cells
