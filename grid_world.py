import numpy as np

def find_grid_position(arr, tar):
    """ 
    function used to find the row and column of an element in the 2d matrix (only for searching unique element)
    Input:
        arr (2d array) - the Gridworld map
        tar (char) - character needed to be found, e.g., 'R'
    Output:
        (i, row.index(tar)) - row and column of the input character on the map
    """
    try:
        for i, row in enumerate(arr):
            if tar in row:
                return (i, row.index(tar)) # return the index of the row (i) and column (row.index(tar))
    except ValueError:
        raise ValueError("Invalid Grid Value!") # if not found, raise the error
        

# Grid World Definition for Part 1
class Grid:
    def __init__(self):
        # set up parameters
        self.number_of_rows = 5
        self.number_of_columns = 5
        self.number_of_states = self.number_of_rows * self.number_of_columns
        self.number_of_actions = 4

        # Actions that agent can take
        #                      left      down      right     up
        self.action =       [ [0, -1],  [1, 0],   [0, 1],   [-1, 0]]
        self.action_text =  ['←', '↓', '→', '↑']

        # Gridworld map
        #             0   1   2   3   4
        self.map = [['T','W','W','W','T'], # 0
                    ['W','W','W','W','W'], # 1
                    ['R','R','W','R','R'], # 2      
                    ['W','W','W','W','W'], # 3 
                    ['B','W','W','W','W']] # 4

        '''
        Moddel structure: number of states by number of actions by n by 4 array
        For one state s and action a, there are n possibilities for transiting to different next state s_,
        each grid position composed of (p, s_, r, t):
            p  - transition probability from (s,a) to (s_)
            s_ - next state
            r  - reward of the transition from (s,a) to (s_)
            t  - terminal information, a bool value, True/False
        The model is used to store the transition probabilities, next states, rewards, and terminal states
        for each state-action pair.
        '''
        # Define the initial state "B"
        row_0, col_0 = find_grid_position(self.map, 'B')
        self.state_0 = row_0 * self.number_of_rows + col_0  # calculate the state number based on the place on the map

        self.model = [[[] for _ in range(self.number_of_actions)] for _ in range(self.number_of_states)]  # Initialize model with empty lists for each (state, action) pair
        for s in range(self.number_of_states):  # Iterate through all possible states
            for a in range(self.number_of_actions):  # Iterate through all possible actions
                row, col = np.divmod(s, self.number_of_rows)  # Convert state index to (row, col) position on the map
                act = self.action[a]  # Get action direction: 0=left, 1=down, 2=right, 3=up
                row_, col_ = row + act[0], col + act[1]  # Calculate the new position after taking action
                state_ = row_ * self.number_of_rows + col_  # Convert new (row_, col_) back to state index
                outsidecheck = (row_ < 0) or (col_ < 0) or (row_ > self.number_of_rows - 1) or (col_ > self.number_of_columns - 1)  # Check if new position is out of bounds

                # Blue cell logic
                if self.map[row][col] == 'B':  # If current cell is Blue
                    if outsidecheck:  # If action goes outside grid
                        self.model[s][a].append([1.0, s, -1.0, False])  # Stay in current state, penalty -1
                    else:  # Valid move within bounds
                        self.model[s][a].append([1.0, state_, -1.0, False])  # Move to new state with penalty -1

                # White cell logic
                elif self.map[row][col] == 'W':  # If current cell is White
                    if outsidecheck:  # If action goes outside grid
                        self.model[s][a].append([1.0, s, -1.0, False])  # Stay in current state, penalty -1
                    elif self.map[row_][col_] == 'R':  # If next cell is Red
                        self.model[s][a].append([1.0, self.state_0, -20.0, False])  # Reset to initial state with heavy penalty
                    elif self.map[row_][col_] == 'T':  # If next cell is Terminal
                        self.model[s][a].append([1.0, state_, -1.0, True])  # Move to terminal with penalty -1, mark as done
                    else:  # Normal move
                        self.model[s][a].append([1.0, state_, -1.0, False])  # Move to new state with penalty -1

                # Red cell logic
                elif self.map[row][col] == 'R':  # If current cell is Red
                    self.model[s][a].append([1.0, s, 0.0, False])  # Stay in place with no reward or terminal flag

                # Terminal cell logic
                elif self.map[row][col] == 'T':  # If current cell is Terminal
                    self.model[s][a].append([1.0, s, 0.0, True])  # Stay in place, zero reward, mark as done

                else:
                    raise ValueError("Invalid grid value!")  # Raise error if an undefined cell type is encountered
