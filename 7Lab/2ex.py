import pygame

pygame.init()

music_list = ["music/3787_new-rington.ru_.mp3", "music/3813_new-rington.ru_.mp3"]
current_music = 0
screen = pygame.display.set_mode((400,600))
pygame.mixer.music.load(music_list[current_music])

key_map = {
    pygame.K_SPACE: "play_pause",
    pygame.K_s: "stop",
    pygame.K_n: "next",
    pygame.K_p: "previous"
}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key in key_map:
                if key_map[event.key] == "play_pause":
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                elif key_map[event.key] == "stop":
                    pygame.mixer.music.stop()
                elif key_map[event.key] == "next":
                    current_music = (current_music + 1) % len(music_list)
                    pygame.mixer.music.load(music_list[current_music])
                    pygame.mixer.music.play()
                elif key_map[event.key] == "previous":
                    current_music = (current_music - 1) % len(music_list)
                    pygame.mixer.music.load(music_list[current_music])
                    pygame.mixer.music.play()
                    
    pygame.time.Clock().tick(30)