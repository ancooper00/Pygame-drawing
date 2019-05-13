#house picture

import pygame
import math

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "My House"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
GRASS = (38, 99, 34)
SKY = (103, 158, 247)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (234, 230, 16)
RED = (234, 16, 16)
BROWN = (76, 30, 3)
GREEN = (13, 61, 35)
LIGHT_BLUE = (189, 204, 196)
    
def draw_house(x, y):
    pygame.draw.rect(screen, WHITE, [x+50, y+100, 200, 200])
    pygame.draw.polygon(screen, RED, [[x, y+100], [x+300, y+100], [x+150, y]])
    pygame.draw.rect(screen, RED, [x+195, y+25, 40, 50])
    pygame.draw.rect(screen, BROWN, [x+125, y+225, 50, 75])
    pygame.draw.rect(screen, LIGHT_BLUE, [x+80, y+140, 50, 65])
    pygame.draw.rect(screen, LIGHT_BLUE, [x+170, y+140, 50, 65])
    pygame.draw.ellipse(screen, YELLOW, [x+160, y+260, 7, 7])

def draw_cloud(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, 100, 70])
    pygame.draw.ellipse(screen, WHITE, [x-25, y-3, 75, 75])
    pygame.draw.ellipse(screen, WHITE, [x+70, y-3, 75, 75])
    pygame.draw.ellipse(screen, WHITE, [x+20, y-23, 80, 75])

def draw_sky(color):
    screen.fill(color)

def draw_grass(x, y):
    pygame.draw.rect(screen, GRASS, [x, y, 800, 150])

def draw_bush(x, y):
    pygame.draw.rect(screen, GREEN, [x+10, y+10, 50, 20])
    pygame.draw.ellipse(screen, GREEN, [x, y+10, 40, 20])
    pygame.draw.ellipse(screen, GREEN, [x+30, y+10, 40, 20])
    pygame.draw.ellipse(screen, GREEN, [x+20, y, 40, 20])

def draw_tree(x, y):
    pygame.draw.rect(screen, BROWN, [x+65, y+55, 30, 125])
    pygame.draw.ellipse(screen, GREEN, [x+35, y+45, 90, 90])
    pygame.draw.ellipse(screen, GREEN, [x, y+30, 90, 90])
    pygame.draw.ellipse(screen, GREEN, [x+70, y+30, 90, 90])
    pygame.draw.ellipse(screen, GREEN, [x+40, y, 90, 90])

def draw_sun(x, y):
    pygame.draw.ellipse(screen, YELLOW, [x, y, 200, 200])
    
# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    # drawing code
    draw_sky(SKY)
    
    draw_sun(-100, -100)
    
    draw_cloud(180, 123)
    draw_cloud(560, 100)
    
    draw_grass(0, 450)
    
    draw_house(400, 150)
    
    draw_bush(430, 420)
    draw_bush(600, 420)
    
    draw_tree(195, 270)
   
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
