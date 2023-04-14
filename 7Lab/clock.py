import pygame
import time

pygame.init()

# Set up the window
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mickey Mouse Clock")

# Load the images for the clock hands
mickey =  pygame.image.load("mickeyclock.jpeg")
mickey = pygame.transform.scale(mickey, screen.get_rect().size)
minute_hand = pygame.image.load("8ef54cc2-176c-4ee7-9f99-53a1650a8eec-transformed.png")
second_hand = pygame.image.load("8ef54cc2-176c-4ee7-9f99-53a1650a8eec-transformed.png")

# Set the origin point for the clock hands
minute_hand = pygame.transform.scale(minute_hand, ((minute_hand.get_rect().size[0] * 0.5), minute_hand.get_rect().size[1] * 0.5))
second_hand = pygame.transform.scale(second_hand, ((second_hand.get_rect().size[0] * 0.5), second_hand.get_rect().size[1] * 0.2))
minute_hand_rect = minute_hand.get_rect(center=(screen_width//2, screen_height//2))
second_hand_rect = second_hand.get_rect(center=(screen_width//2, screen_height//2))
# minute_hand = pygame.transform.scale(minute_hand, ((minute_hand.get_rect().size[0] * 0.3), minute_hand.get_rect().size[1] * 0.3))

# Set the clock font and font size
clock_font = pygame.font.Font(None, 50)

# Main game loop
while True:
    # Handle events (such as quitting the game) here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.blit(mickey, (0, 0))
    # Get the current time in seconds and minutes
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    # Rotate the clock hands based on the current time
    minute_hand_rotated = pygame.transform.rotate(minute_hand, -minutes * 6)
    second_hand_rotated = pygame.transform.rotate(second_hand, -seconds * 6 - 96)

    # Set the new positions of the clock hands
    minute_hand_rect = minute_hand_rotated.get_rect(center=minute_hand_rect.center)
    second_hand_rect = second_hand_rotated.get_rect(center=second_hand_rect.center)

    # Clear the screen and draw the clock hands
    # screen.fill((255, 255, 255))
    screen.blit(minute_hand_rotated, minute_hand_rect)
    screen.blit(second_hand_rotated, second_hand_rect)

    # Display the current time in the top left corner
    current_time_str = f"{minutes:02}:{seconds:02}"
    current_time_text = clock_font.render(current_time_str, True, (0, 0, 0))
    screen.blit(current_time_text, (10, 10))

    # Update the screen
    pygame.display.update()
