class ModelBasedAgent:
    def __init__(self, environment):
        self.env = environment
        # Start at a random location in the grid
        self.x, self.y = np.random.randint(0, self.env.M), np.random.randint(0, self.env.N)
        # Initialize an internal model of the environment as an empty grid
        self.model = np.zeros((self.env.M, self.env.N))
        self.visited_space = np.zeros((self.env.M, self.env.N))

    def update_model(self):
        """
        This method should update the agent's internal model of the environment.
        You can use this to store information about what the agent has observed
        so far (e.g., whether there is dirt at a particular location).

        Suggestions:
        - Store the current status of the environment in self.model.
        - Keep track of visited locations and dirt information.
        - Update the model based on the agent's current perception of its surroundings.
        """

        # Update the model with the current environment state
        self.model[self.x, self.y] = self.env.grid[self.x, self.y]

        self.visited_space[self.x, self.y] = 1



    def act(self):
        """
        This method should define the agent's actions at each step. Typically, the agent will:
        - Update its internal model (using update_model).
        - Decide where to move next or whether to suck up dirt.
        - Move to a new location (using the move method) or clean the current location.

        Suggestions:
        - Use the information from the model to make decisions.
        - Try to balance exploration of new areas with cleaning known dirty areas.
        """
        self.update_model()

        # Add decision-making logic here based on the model
        if self.env.grid[self.x, self.y] > 0:
            self.suck()
        else:
            self.move()

    def move(self):
        """
        This method should define how the agent moves to a neighboring location.

        Suggestions:
        - The agent must move based on the model's information (e.g., to a dirty location).
        - Ensure the agent doesn't move outside the bounds of the grid.
        - Update the agent's position (self.x, self.y) based on its movement.
        """
        moves = []


        # Possible agent's move based on the chosen direction, the x-axis and y-axis get updated
        # At the same time, ensuring it doesn't go out of bounds

        if self.x > 0:
            moves.append(('up', self.x - 1, self.y))
        if self.x < self.env.M - 1:
            moves.append(('down', self.x + 1, self.y))
        if self.y > 0:
            moves.append(('left', self.x, self.y - 1))
        if self.y < self.env.N - 1:
            moves.append(('right', self.x, self.y + 1))


        unvisited_moves = []

        # Check if there are unvisited moves
        unvisited_moves = [move for move in moves if self.visited_space[move[1], move[1]] == 0]

        if unvisited_moves:
          dirty_unvisited_moves = [move for move in unvisited_moves if self.model[move[1], move[1]] > 0]
          if dirty_unvisited_moves:
            move = dirty_unvisited_moves[0]
          else:
            move = unvisited_moves[0]

        else:
          dirty_move = [move for move in moves if self.model[move[1], move[2]] > 0]
          if dirty_move:
            move = dirty_move[0]
          else:
            move = moves[0]

        direction,new_x,new_y = move
        self.x, self.y = new_x, new_y

        # Mark the new location as visited
        self.visited_space[self.x, self.y] = 1

    def suck(self):
        """
        This method makes the agent clean its current location by setting the grid cell to 0 (clean).
        No changes are needed here, as this method is already functional.
        """
        self.env.grid[self.x, self.y] = 0  # Clean the current cell
