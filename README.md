# Sudoku

## Setup
- Install [GitHub CLI](https://cli.github.com/) and connect it with GitHub account
- Open up Git CMD
- Run `gh repo clone johann017/Sudoku` in the command line

`Sudoku.py`:
- To run this, type the following in to the command line:
  ```
  python Sudoku.py
  ```
  
`SudokuGUI.py`:
- To run this, type the following in to the command line:
  ```
  python SudokuGUI.py
  ```


## Description
This project features two parts: a Sudoku solver and a GUI meant for users to play with. The Sudoku solver utilizes the backtracking algorithm in which the algorithm goes back one step if the previous step is wrong and uses that to determine a solution for the given board. The GUI displays the board and offers an interactive interface which allows users to click and type their answers out and the GUI will display a red X if the solution present is wrong and place it in the square if it is correct.
