import pygame
import time

pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mickey Mouse Clock")

mickey =  pygame.image.load("mickeyclock.jpeg")
mickey = pygame.transform.scale(mickey, screen.get_rect().size)
minute_hand = pygame.image.load("8ef54cc2-176c-4ee7-9f99-53a1650a8eec-transformed.png")
second_hand = pygame.image.load("8ef54cc2-176c-4ee7-9f99-53a1650a8eec-transformed.png")

minute_hand = pygame.transform.scale(minute_hand, ((minute_hand.get_rect().size[0] * 0.5), minute_hand.get_rect().size[1] * 0.5))
second_hand = pygame.transform.scale(second_hand, ((second_hand.get_rect().size[0] * 0.5), second_hand.get_rect().size[1] * 0.2))
minute_hand_rect = minute_hand.get_rect(center=(screen_width//2, screen_height//2))
second_hand_rect = second_hand.get_rect(center=(screen_width//2, screen_height//2))

clock_font = pygame.font.Font(None, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.blit(mickey, (0, 0))
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    minute_hand_rotated = pygame.transform.rotate(minute_hand, -minutes * 6)
    second_hand_rotated = pygame.transform.rotate(second_hand, -seconds * 6 - 96)

    minute_hand_rect = minute_hand_rotated.get_rect(center=minute_hand_rect.center)
    second_hand_rect = second_hand_rotated.get_rect(center=second_hand_rect.center)


    screen.blit(minute_hand_rotated, minute_hand_rect)
    screen.blit(second_hand_rotated, second_hand_rect)

    current_time_str = f"{minutes:02}:{seconds:02}"
    current_time_text = clock_font.render(current_time_str, True, (0, 0, 0))
    screen.blit(current_time_text, (10, 10))


    pygame.display.update()