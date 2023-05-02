import pygame
import random

pygame.init()
pygame.font.init()

screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
N=0
U=0
A=0
f1 = pygame.font.Font(None, 36)
text1 = f1.render("Счет:" + str(N) + "  Уровень:" + str(U), True, (180, 0, 0))


screen.blit(text1, (0, 0))


snake = [(screen_width // 2, screen_height // 2)]
food = [(random.randint(0, (screen_width-20) // 10) * 10, random.randint(10, (screen_height-20) // 10) * 10)]

direction = 'right'
game_over = False

speed = 0

clock = pygame.time.Clock()

while not game_over:
    clock.tick(10+speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'
            elif event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'
            elif event.key == pygame.K_UP and direction != 'down':
                direction = 'up'
            elif event.key == pygame.K_DOWN and direction != 'up':
                direction = 'down'
    
    if snake[0][0] + 10 > 630 or snake[0][0] - 10 < 0 or snake[0][1] - 10 < 20 or snake[0][1] + 10 > 470:
        while not game_over:
            screen.fill(RED)
            clock.tick(10+speed)
            food = [(random.randint(0, (screen_width-20) // 10) * 10, random.randint(10, (screen_height-20) // 10) * 10)]
            speed = 0
            N = 0
            U = 0
            screen.fill(RED)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        snake = [(screen_width // 2, screen_height // 2)]
                        snake_length = 1
                elif event.type == pygame.QUIT:
                    exit()

    for i in range(1, len(snake)):
        if snake[0] == snake[i]:
            while not game_over:
                food = [(random.randint(0, (screen_width-20) // 10) * 10, random.randint(10, (screen_height-20) // 10) * 10)]
                snake = [(screen_width // 2, screen_height // 2)]
                speed = 0
                N = 0
                U = 0
                screen.fill(RED)
                clock.tick(10)
                screen.fill(RED)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                    elif event.type == pygame.QUIT:
                        exit()
    text1 = f1.render("Счет:" + str(N) + "  Уровень:" + str(U), True, (180, 0, 0))
    game_over = False
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
        food = [(random.randint(0, (screen_width-20) // 10) * 10, random.randint(10, (screen_height-20) // 10) * 10)]
        N+=1
        A+=1
        if A>=4:
            U+=1
            A=0
            speed+=2
    else:
        snake.pop() 
    text1 = f1.render("Счет:" + str(N) + "  Уровень:" + str(U), True, (180, 0, 0))
    screen.fill((0, 0, 0))
    for segment in snake:
        pygame.draw.rect(screen, (255, 255, 255), (segment[0], segment[1], 10, 10))
    pygame.draw.rect(screen, (255, 0, 0), (food[0][0], food[0][1], 10, 10))
    screen.blit(text1, (0, 0))
    pygame.display.update()

pygame.quit()