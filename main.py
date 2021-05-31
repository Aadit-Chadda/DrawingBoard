import pygame

pygame.init()

# Dimensions
width = 1000

draw_display = pygame.display.set_mode((width, width))
pygame.display.set_caption('White-Board')

# Defining colors
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


class Draw:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.width = width
        self.total_rows = total_rows
    
    def get_pos(self):
        return self.row, self.col
    
    def reset(self):
        self.color = WHITE
    
    def colored(self):
        return self.color == BLACK
    
    def is_line(self):
        return self.color == BLACK
    
    def make_line(self):
        self.color = BLACK

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))


def make_grid(rows, width):
    grid = []
    gap = width//rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Draw(i, j, gap, rows)
            grid[i].append(node)
    return grid


def draw_grid(draw_display, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(draw_display, WHITE, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(draw_display, WHITE, (j * gap, 0), (j * gap, width))


def draw(draw_display, grid, rows, width):
    draw_display.fill(WHITE)
    
    for row in grid:
        for node in row:
            node.draw(draw_display)
    
    draw_grid(draw_display, rows, width)
    pygame.display.update()

   
def get_clicked_pos(pos, rows, width):
    gap = width / rows
    y, x = pos
    
    row = y // gap
    col = x // gap
    
    return row, col


# Starting Mainloop
def main(draw_display, width):
    ROWS = 100
    grid = make_grid(ROWS, width)
    run = True
    while run:
        draw(draw_display, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if pygame.mouse.get_pressed()[0]:  # LEFT Click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.make_line()
            
            elif pygame.mouse.get_pressed()[2]: # RIGHT Click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
            
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    grid = make_grid(ROWS, width)
                
    pygame.quit()


main(draw_display, width)
