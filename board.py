# making imports
import pygame
import math
from queue import PriorityQueue

# Creating window
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("WhiteBoard")

# Node-run colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


# Defining game class
class Spot:
    # Initiating base
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
    
    # Getting position of node
    def get_pos(self):
        return self.row, self.col
    
    # Defining which nodes have been checked before
    def is_closed(self):
        return self.color == RED
    
    # Defining if a node is open
    def is_open(self):
        return self.color == GREEN
    
    # Defining the barrier(End-point) of nodes on window
    def is_barrier(self):
        return self.color == BLACK
    
    # Defining the START node
    def is_start(self):
        return self.color == ORANGE
    
    # Defining the END node
    def is_end(self):
        return self.color == TURQUOISE
    
    # Resetting Node value
    def reset(self):
        self.color = WHITE
    
    # Making START node
    def make_start(self):
        self.color = ORANGE
    
    # Making CLOSED nodes
    def make_closed(self):
        self.color = RED
    
    # Making OPEN nodes
    def make_open(self):
        self.color = GREEN
    
    # Making barrier nodes
    def make_barrier(self):
        self.color = BLACK
    
    # Making the end-node
    def make_end(self):
        self.color = TURQUOISE
    
    # Defining the Path of Scratch
    def make_path(self):
        self.color = PURPLE
    
    # Re-presentation on screen
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))


# Representing grid on screen
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, WHITE, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, WHITE, (j * gap, 0), (j * gap, width))


# Representing work done by AI agent during the run
def draw(win, grid, rows, width):
    win.fill(WHITE)
    
    for row in grid:
        for spot in row:
            spot.draw(win)
    
    draw_grid(win, rows, width)
    pygame.display.update()


# Making selection of START POINT, END POINT and obstructions in the path of the AI
def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    
    row = y // gap
    col = x // gap
    
    return row, col


# Starting main-loop
def main(win, width):
    ROWS = 100
    grid = make_grid(ROWS, width)
    
    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if pygame.mouse.get_pressed()[0]:  # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.make_barrier()
            
            elif pygame.mouse.get_pressed()[2]:  # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
    
    pygame.quit()


main(WIN, WIDTH)