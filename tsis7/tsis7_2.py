import pygame

def next_song():
    global songs
    songs = songs[1:] + [songs[0]]
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()

def prev_song():
    global songs
    songs = [songs[-1]] + songs[:-1]
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()

pygame.init()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.FULLSCREEN)
done = False
clock = pygame.time.Clock()
songs = ['music/Blue Bird by Ikimonogakari.mp3', 
    'music/My War by Shinsei Kamattechan.mp3', 
    'music/Shinzou Wo Sasageyo by Linked Horizon.mp3']
current_song = None
SONG_END = pygame.USEREVENT
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
on_pause = True

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == SONG_END:
            next_song()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                next_song()
            if event.key == pygame.K_LEFT:
                prev_song()
            if event.key == pygame.K_SPACE:
                if on_pause:
                    pygame.mixer.music.unpause()
                    on_pause = False
                else:
                    pygame.mixer.music.pause()
                    on_pause = True
            
    screen.fill((255, 255, 255))

    pygame.display.flip()
    clock.tick(60)