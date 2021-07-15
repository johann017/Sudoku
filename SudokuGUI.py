import pygame
from Sudoku import solve, exist
import time
pygame.font.init()

##**Inspired by Tech with Tim**##


class Cube:
    rows = 9
    cols = 9
    
    #Sets variables to their default
    def __init__(self, value, row, col, width ,height):
        self.value = value
        self.temp = -1
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    #Draws the 3X3 squares
    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != -1 and self.value == -1:
            text = fnt.render(str(self.temp), 1, (128,128,128))
            win.blit(text, (x+5, y+5))
        elif not(self.value == -1):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))
            
        if self.selected:
            pygame.draw.rect(win, (255,0,0), (x,y, gap ,gap), 3)

    def set(self, val):
        self.value = val

    def set_temp(self, val):
        self.temp = val


class Grid:
    #Original grid
    board = [
    [-1,-1,-1,-1,-1,5,-1,-1,4],
    [2,-1,8,-1,-1,-1,6,-1,9],
    [9,-1,5,4,2,-1,-1,-1,7],
    [-1,7,-1,-1,5,4,2,6,-1],
    [-1,-1,4,-1,6,-1,8,-1,-1],
    [-1,2,3,7,1,-1,-1,9,-1],
    [7,-1,-1,-1,4,3,9,-1,8],
    [3,-1,9,-1,-1,-1,5,-1,2],
    [4,-1,-1,5,-1,-1,-1,-1,-1]
    ]

    #Initializes variables
    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

    #Redraws all 9 cubes which each contain a 3X3 grid of squares
    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    #This handles placing a vlue into the board and checking if it is correct
    def place(self, val):
        row, col = self.selected
        if self.cubes[row][col].value == -1:
            self.cubes[row][col].set(val)
            self.update_model()
            if not exist(self.model, val, row,col) and solve(self.model): 
                return True
            else:
                self.cubes[row][col].set(-1)
                self.cubes[row][col].set_temp(-1)
                self.update_model()
                return False
            
    #This handles when the square is selected and a value is given
    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    #Draws the whole 9X9 grid
    def draw(self, win):
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 10
            else:
                thick = 1
            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

    #Handles when a square is selected            
    def select(self, row, col):
        # Reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    #Clears the square by setting value to -1
    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == -1:
            self.cubes[row][col].set_temp(-1)

    #Handles the instance a square is clicked
    def click(self, pos):
        """
        :param: pos
        :return: (row, col)
        """
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y),int(x))
        else:
            return None

    #Checks if all the squares have a value
    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == -1:
                    return False
        return True

#Redraws the whole window
def redraw_window(win, board, time, strikes):
    win.fill((255,255,255))
    # Draw time
    fnt = pygame.font.SysFont("comicsans", 40)
    text = fnt.render("Time: " + format_time(time), 1, (0,0,0))
    win.blit(text, (360, 560))
    # Draw Strikes
    text = fnt.render("X " * strikes, 1, (255, 0, 0))
    win.blit(text, (20, 560))
    # Draw grid and board
    board.draw(win)

#Draws the time in corner
def format_time(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat


def main():
    win = pygame.display.set_mode((540,600))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540)
    key = None
    run = True
    start = time.time()
    strikes = 0
    while run:
        
        #Time elapsed
        play_time = round(time.time() - start)

        for event in pygame.event.get():
            #Gets the user input
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                #If the user hits return it places the number on the board
                #and checks with the answer key which was generated in the background.
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    
                    #Checks the validity of the user's input
                    if board.cubes[i][j].temp != -1:
                        if board.place(board.cubes[i][j].temp):
                            print("Success")
                        else:
                            print("Wrong")
                            strikes += 1
                        key = None
                        
                        #Checks if board is done
                        if board.is_finished():
                            print("Game over")
                            run = False
                            
            #Gets is the user clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            board.sketch(key)
        
        #Keeps redrawing board and updating in the background
        redraw_window(win, board, play_time, strikes)
        pygame.display.update()

main()
pygame.quit()
