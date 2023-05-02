import pygame

# initialize Pygame
pygame.init()

# create a window
screen = pygame.display.set_mode((800, 600))

# set the title of the window
pygame.display.set_caption("Paint")

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# set default drawing color
DRAW_COLOR = BLACK

# set default tool
TOOL = "PEN"

# set default line width
LINE_WIDTH = 1

# create virtual buttons
button_pen = pygame.Rect(10, 10, 50, 50)
button_rect = pygame.Rect(70, 10, 50, 50)
button_circle = pygame.Rect(130, 10, 50, 50)
button_eraser = pygame.Rect(190, 10, 50, 50)
button_black = pygame.Rect(250, 10, 50, 50)
button_red = pygame.Rect(310, 10, 50, 50)
button_green = pygame.Rect(370, 10, 50, 50)
button_blue = pygame.Rect(430, 10, 50, 50)
button_yellow = pygame.Rect(490, 10, 50, 50)

# function to draw the virtual buttons
def draw_buttons():
    pygame.draw.rect(screen, BLACK, button_pen, width=2)
    pygame.draw.rect(screen, BLACK, button_rect, width=2)
    pygame.draw.rect(screen, BLACK, button_circle, width=2)
    pygame.draw.rect(screen, BLACK, button_eraser, width=2)
    pygame.draw.rect(screen, BLACK, button_black, width=2)
    pygame.draw.rect(screen, BLACK, button_red, width=2)
    pygame.draw.rect(screen, BLACK, button_green, width=2)
    pygame.draw.rect(screen, BLACK, button_blue, width=2)
    pygame.draw.rect(screen, BLACK, button_yellow, width=2)
    pygame.draw.line(screen, DRAW_COLOR, (15, 35), (45, 35), width=3)
    pygame.draw.rect(screen, DRAW_COLOR, (75, 20, 30, 30))
    pygame.draw.circle(screen, DRAW_COLOR, (150, 35), 15)
    pygame.draw.rect(screen, WHITE, (195, 25, 20, 20), width=2)
    pygame.draw.rect(screen, BLACK, (197, 27, 16, 16), width=1)
    pygame.draw.rect(screen, BLACK, button_black)
    pygame.draw.rect(screen, RED, button_red)
    pygame.draw.rect(screen, GREEN, button_green)
    pygame.draw.rect(screen, BLUE, button_blue)
    pygame.draw.rect(screen, YELLOW, button_yellow)
    

# create a surface to draw on
canvas = pygame.Surface((800, 600))

# define a variable to keep track of whether the user is holding down the mouse button
drawing = False

# define a variable to keep track of the previous position of the mouse
last_pos = None

# main game loop
while True:
    # handle events
    for event in pygame.event.get():
        # check if the user clicked the close button
        if event.type == pygame.QUIT:
            # exit the main loop and close the window
            pygame.quit()
            exit()
    
    # clear
