import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set the size of the window
window_size = (1500, 1500)
screen = pygame.display.set_mode(window_size)

# Load the image of Mickey Mouse
mickey_image = pygame.image.load('7Lab/images/mickeyclock.jpeg')
mickey_rect = mickey_image.get_rect(center=(250, 250))

# Set the clock font and size
clock_font = pygame.font.SysFont('comicsansms', 60)

# Set the initial angle of the hands
minute_angle = 0
second_angle = 0

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current time
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Calculate the angle of the hands
    minute_angle = -6 * minutes
    second_angle = -6 * seconds

    # Rotate the hands
    minute_hand = pygame.transform.rotate(mickey_image, minute_angle)
    second_hand = pygame.transform.rotate(mickey_image, second_angle)

    # Blit the hands on the screen
    screen.fill((255, 255, 255))
    screen.blit(minute_hand, mickey_rect)
    screen.blit(second_hand, mickey_rect)

    # Update the display
    pygame.display.update()
    pygame.time.delay(1000)  # Wait for 1 second before updating the clock
