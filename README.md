# Sudoku

## Description
- #### Overview: 
    - This project features a Sudoku solver and a GUI where users can play.
- #### Details: 
    - The Sudoku solver utilizes the backtracking algorithm that goes back a step if the previous step is wrong and determines the solution for the given board. The GUI displays the board and offers an interactive interface where users can input their answers. If the answer is correct, the GUI places the value in the square, else it displays a red X instead.
    
<h3 align="center">GUI Board</h3>    
<p align="center">
   <img src="https://github.com/johann017/Sudoku/blob/22c2899e21ec943ff8df87d246e701dee6d66c53/Screenshots/SudokuBoard.PNG" width = "250"     height = "250"/>
</p>

<h3 align="center">Incorrect Placement (User places a 1 in the second square) </h3>
<p align="center">
   <img src="https://github.com/johann017/Sudoku/blob/9bf7a2a44c3106e9e2e905712db680b2249a769d/Screenshots/Incorrect.PNG" width = "250"     height = "250"/>
</p>

<h3 align="center">Correct Placement (As a next move,user places a 1 in the first square)</h3>
<p align="center">
   <img src="https://github.com/johann017/Sudoku/blob/9bf7a2a44c3106e9e2e905712db680b2249a769d/Screenshots/Correct.PNG" width = "250"     height = "250"/>
</p>

## Setup
- Install [GitHub CLI](https://cli.github.com/) and connect to GitHub account
- Open Git CMD
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
