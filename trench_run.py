# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "TRENCH RUN"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
WALL_GRAY = (94, 97, 102)
FLOOR_GRAY = (114, 115, 117)
ACCENT_GRAY_DARK = (46, 47, 48)
ACCENT_GRAY_LIGHT = (147, 148, 150)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (163, 58, 6)
BLUE = (6, 76, 107)
XWING_GRAY = (202, 204, 206)
EXHUAST = (188, 52, 111)

    

def draw_background(x, y):
    screen.fill(BLACK)

def draw_stars(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, 7, 7])

def draw_floor(x, y):
    pygame.draw.polygon(screen, FLOOR_GRAY, [[x, y], [x+200, y-175],[x+200, y]])
    pygame.draw.rect(screen, FLOOR_GRAY, [x+200, y-175, 100, 175])
    pygame.draw.polygon(screen, FLOOR_GRAY, [[x+300, y], [x+300, y-175],[x+500, y]])

def draw_right_wall(x, y):
    pygame.draw.polygon(screen, WALL_GRAY, [[x,
    y], [x, y-75],[x+350, y-300], [x+350, y+175], [x+200, y+175]])

def draw_left_wall(x, y):
    pygame.draw.polygon(screen, WALL_GRAY, [[x,
    y], [x, y-75],[x-350, y-300], [x-350, y+175], [x-200, y+175]])

def draw_yavin(x, y):
    pygame.draw.ellipse(screen, ORANGE, [x, y, 100, 100])

def draw_moon(x, y):
    pygame.draw.ellipse(screen, BLUE, [x, y, 35, 35])

def draw_xwing(x, y):
    pygame.draw.polygon(screen, XWING_GRAY, [[x, y], [x+20, y-60], [x+95, y-60], [x+115, y]])
    pygame.draw.polygon(screen, XWING_GRAY, [[x, y], [x+20, y+80], [x+95, y+80], [x+115, y]])
    pygame.draw.polygon(screen, ACCENT_GRAY_DARK, [[x+10, y], [x+30, y-50], [x+85, y-50], [x+105, y]])
    pygame.draw.polygon(screen, ACCENT_GRAY_DARK, [[x+10, y], [x+30, y+70], [x+85, y+70], [x+105, y]])

    pygame.draw.line(screen, XWING_GRAY, [x+107,y-30], [x+260, y-70], 15)
    pygame.draw.line(screen, XWING_GRAY, [x+107,y+30], [x+260, y+70], 15)
    pygame.draw.line(screen, XWING_GRAY, [x+10,y-30], [x-145, y-70], 15)
    pygame.draw.line(screen, XWING_GRAY, [x+10,y+30], [x-145, y+70], 15)

        
    pygame.draw.ellipse(screen, XWING_GRAY, [x-35, y-60, 50, 50])
    pygame.draw.ellipse(screen, XWING_GRAY, [x-35, y+10, 50, 50])
    pygame.draw.ellipse(screen, XWING_GRAY, [x+100, y-60, 50, 50])
    pygame.draw.ellipse(screen, XWING_GRAY, [x+100, y+10, 50, 50])
    pygame.draw.ellipse(screen, EXHUAST, [x-31, y-56, 45, 45])
    pygame.draw.ellipse(screen, EXHUAST, [x-31, y+12, 45, 45])
    pygame.draw.ellipse(screen, EXHUAST, [x+104, y-58, 45, 45])
    pygame.draw.ellipse(screen, EXHUAST, [x+104, y+12, 45, 45])

    pygame.draw.ellipse(screen, WALL_GRAY, [x+35, y-25, 45, 45])

 
    
# Game loop
done = False

luke_x = 345
luke_y = 430

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Pew!")

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        luke_y -= 2
    elif pressed[pygame.K_DOWN]:
        luke_y += 2
    elif pressed[pygame.K_LEFT]:
        luke_x -= 2
    elif pressed[pygame.K_RIGHT]:
        luke_x += 2


    #drawing code

    draw_background(0,0)
    draw_stars(100, 100)
    draw_stars(130, 200)
    draw_stars(450, 80)
    draw_stars(310, 300)
    draw_stars(700, 230)
    draw_stars(780, 120)
    draw_stars(640, 210)
    draw_stars(530, 210)
    draw_stars(270, 170)
    draw_stars(320, 95)
    draw_stars(680, 120)
    draw_stars(450, 210)
    draw_stars(525, 210)
    draw_stars(320, 200)
    
    draw_yavin(560, 75)
    draw_moon(670, 150)

    draw_floor(150, 600)
    draw_right_wall(450, 425)
    draw_left_wall(350, 425)

    draw_xwing(luke_x, luke_y)

    

    

  
    

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()

