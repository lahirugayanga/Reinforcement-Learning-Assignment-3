# Simulation code of the assignment:

## Prerequisites <a name="prerequisites"></a>
- **Python 3.12**
- **Jupyter Notebook**

To run the code, install the following packages with their specified versions:
***
You have to install: 
1. **ipykernel**  
   ```bash
   pip install ipykernel==6.29.5
   ```
2. **numpy**  
   ```bash
   pip install numpy==2.3.2
   ```
4. **matplotlib**  
   ```bash
   pip install matplotlib==3.10.5
   ```

***
## Code Files

### 1. `grid_world.py`
**Description**:  
Contains the definition of the two Grid Worlds used in:
- Sarsa Algorithm
- Q-learning Algorithm

---

### 2. `main.ipynb`
**Description**:  
Trains agents using both SARSA and Q-learning to learn optimal policies in the gridworld environment and compares their performance.

**Functionality Includes**:
- Learning optimal policies using: SARSA algorithm, Q-learning algorithm
- Policy visualization via symbol maps
- Trajectory generation from learned policies
- Reward tracking across episodes

**Comparison Tasks Implemented**:
- Plot and compare the policies learned by SARSA and Q-learning
- Visualize agent trajectories using the learned policies
- Analyze differences in agent behavior and reward accumulation
- Evaluate which algorithm performs better and explain why

