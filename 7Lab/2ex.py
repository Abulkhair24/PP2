import pygame
import os

pygame.init()

window_title = "My Music Player"
window_size = (640, 480)
background_color = (255, 255, 255)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)
pygame.mixer.init()
music_file = "my_song.mp3"
pygame.mixer.music.load(music_file)
key_play_pause = pygame.K_SPACE
key_stop = pygame.K_s
key_next = pygame.K_RIGHT
key_previous = pygame.K_LEFT
key_quit = pygame.K_q
pygame.mixer.music.play()
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == key_play_pause:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == key_stop:
                pygame.mixer.music.stop()
            elif event.key == key_next:
                pass  # TODO: Implement this
            elif event.key == key_previous:
                pass  # TODO: Implement this
            elif event.key == key_quit:
                pygame.quit()