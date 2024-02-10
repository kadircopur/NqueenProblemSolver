# N-Queen Problem Solver with Hill Climbing Algorithm

This Python script solves the N-Queen problem using a hill climbing algorithm.

## Problem Description

The N-Queen problem is a classic problem in computer science and combinatorial optimization. The objective is to place N queens on an N×N chessboard in such a way that no two queens attack each other. In chess, a queen can attack in all eight directions - horizontally, vertically, and diagonally.

## Algorithm

The script begins by randomly distributing pieces for each column. Then, the solver class starts the hill climbing algorithm. In each iteration, the algorithm calculates the heuristic value for the current state and explores neighboring states by moving a queen to a different row in the same column. It chooses the move that maximizes the heuristic value, aiming to reach the global optimum where no two queens attack each other.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/n-queen-hill-climbing.git
   ```

2. Run the script:

   ```bash
   python3 n_queen_solver.py
   ```

4. Enter the value of N when prompted.

5. The script will display the solution to the N-Queen problem using the hill climbing algorithm.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project was inspired by the need for an efficient N-Queen problem solver using hill climbing algorithm. Special thanks to the Python community for their valuable resources and tutorials on hill climbing algorithms.

---

![1707569070837249](https://github.com/kadircopur/NqueenProblemSolver/assets/77071513/92027eb9-945a-4b64-b0aa-8ffd99334bdd)
