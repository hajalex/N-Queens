# N-Queens

The N-Queens problem is a classic puzzle where you need to place N chess queens on an N×N chessboard in such a way that no two queens threaten each other.

## Overview

This Python code implements the N-Queens problem using local search techniques. It defines a class `NQueensState` that represents a state of the N-Queens problem. Here's an overview of what the code does:

### Import Necessary Libraries

The code imports the following libraries: `math`, `matplotlib.pyplot`, `sys`, and `random`.

### Class `NQueensState`

This class represents a state of the N-Queens problem and manages the state of the board using various methods and attributes:

- `__init__`: Initializes the state. If a list of queens' positions is provided, it uses that list; otherwise, it generates a random initial arrangement of queens.
- `conflicts`: Returns the number of conflicts (threats between queens).
- `_compute_conflicts`: Calculates the number of conflicts between queens and stores it in `num_conflicts`.
- `neighbors`: Generates and yields neighboring states by swapping queens in different positions.
- `best_neighbors`: Returns the best neighboring state with the lowest number of conflicts.
- `random_neighbors`: Returns a random neighboring state obtained by swapping two randomly chosen queens.
- `plot`: Plots the current state of the board, showing queens' positions. It uses `matplotlib` to create a visual representation of the board.

### Creating a State and Plotting

An instance of `NQueensState` is created with N=16, and then its `plot` method is called to visualize the arrangement of queens on the board.

### Visualization

The `plot` method generates a graphical representation of the N-Queens board using `matplotlib`. Queens are represented by "Q" symbols, and conflicts between queens are indicated by their positions.

## Usage

1. Make sure you have the required libraries (`math`, `matplotlib.pyplot`, `sys`, `random`) installed.
2. Clone this repository to your local machine.
3. Run the script using a Python interpreter.
4. Follow the prompts to visualize the N-Queens arrangement and explore different states.

Feel free to use and modify this code according to your needs.
