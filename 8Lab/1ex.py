import pygame
import random

pygame.init()

screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

snake = [(screen_width // 2, screen_height // 2)]
food = [(random.randint(0, screen_width // 10) * 10, random.randint(0, screen_height // 10) * 10)]

direction = 'right'
game_over = False

clock = pygame.time.Clock()

while not game_over:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'
            elif event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'
            elif event.key == pygame.K_UP and direction != 'down':
                direction = 'up'
            elif event.key == pygame.K_DOWN and direction != 'up':
                direction = 'down'

    if direction == 'right':
        new_head = (snake[0][0] + 10, snake[0][1])
    elif direction == 'left':
        new_head = (snake[0][0] - 10, snake[0][1])
    elif direction == 'up':
        new_head = (snake[0][0], snake[0][1] - 10)
    elif direction == 'down':
        new_head = (snake[0][0], snake[0][1] + 10)

    snake.insert(0, new_head)

    if snake[0] == food[0]:
        food = [(random.randint(0, screen_width // 10) * 10, random.randint(0, screen_height // 10) * 10)]
    else:
        snake.pop()

    screen.fill((0, 0, 0))
    for segment in snake:
        pygame.draw.rect(screen, (255, 255, 255), (segment[0], segment[1], 10, 10))
    pygame.draw.rect(screen, (255, 0, 0), (food[0][0], food[0][1], 10, 10))
    pygame.display.update()

pygame.quit()