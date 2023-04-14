import pygame

pygame.init()


WHITE = (255, 255, 255)
RED = (255, 0, 0)


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


BALL_SIZE = 50
BALL_RADIUS = 25
ball_x = (SCREEN_WIDTH - BALL_SIZE) / 2
ball_y = (SCREEN_HEIGHT - BALL_SIZE) / 2


SPEED = 20


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


screen.fill(WHITE)


pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)


pygame.display.update()


running = True
while running:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
        
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
                
            if ball_x < BALL_RADIUS:
                ball_x = BALL_RADIUS
            elif ball_x > SCREEN_WIDTH - BALL_RADIUS:
                ball_x = SCREEN_WIDTH - BALL_RADIUS
            if ball_y < BALL_RADIUS:
                ball_y = BALL_RADIUS
            elif ball_y > SCREEN_HEIGHT - BALL_RADIUS:
                ball_y = SCREEN_HEIGHT - BALL_RADIUS
            
            
            screen.fill(WHITE)
            pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)
            pygame.display.update()


pygame.quit()
