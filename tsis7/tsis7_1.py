import pygame
import os
import datetime

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect)

pygame.init()
screen = pygame.display.set_mode((850, 850))
done = False
clock = pygame.time.Clock()

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_time = datetime.datetime.now()
    seconds = current_time.second
    minutes = current_time.minute

    screen.fill((255, 255, 255))
    screen.blit(get_image('sprites/clock_base.png'), (0, 0))
    blitRotateCenter(screen, get_image('sprites/clock_min.png'), (0, 0), -(minutes * 6))
    blitRotateCenter(screen, get_image('sprites/clock_sec.png'), (0, 0), -(seconds * 6))

    pygame.display.flip()
    clock.tick(60)