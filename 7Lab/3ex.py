import pygame

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Set ball dimensions and starting position
BALL_SIZE = 50
BALL_RADIUS = 25
ball_x = (SCREEN_WIDTH - BALL_SIZE) / 2
ball_y = (SCREEN_HEIGHT - BALL_SIZE) / 2

# Set ball movement speed
SPEED = 20

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set screen background color
screen.fill(WHITE)

# Draw ball on screen
pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

# Update screen
pygame.display.update()

# Game loop
running = True
while running:
    # Check for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Move ball up by SPEED pixels
                ball_y -= SPEED
            elif event.key == pygame.K_DOWN:
                # Move ball down by SPEED pixels
                ball_y += SPEED
            elif event.key == pygame.K_LEFT:
                # Move ball left by SPEED pixels
                ball_x -= SPEED
            elif event.key == pygame.K_RIGHT:
                # Move ball right by SPEED pixels
                ball_x += SPEED
                
            # Check if ball is outside of screen boundaries
            if ball_x < BALL_RADIUS:
                ball_x = BALL_RADIUS
            elif ball_x > SCREEN_WIDTH - BALL_RADIUS:
                ball_x = SCREEN_WIDTH - BALL_RADIUS
            if ball_y < BALL_RADIUS:
                ball_y = BALL_RADIUS
            elif ball_y > SCREEN_HEIGHT - BALL_RADIUS:
                ball_y = SCREEN_HEIGHT - BALL_RADIUS
            
            # Redraw ball at new position
            screen.fill(WHITE)
            pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)
            pygame.display.update()

# Quit Pygame
pygame.quit()
