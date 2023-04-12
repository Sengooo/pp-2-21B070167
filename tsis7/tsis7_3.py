import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False
clock = pygame.time.Clock()
x = 100
y = 100

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_LEFT]:
        x -= 20
        if x < 50:
            x = 50
    if key_input[pygame.K_UP]:
        y -= 20
        if y < 50:
            y = 50
    if key_input[pygame.K_RIGHT]:
        x += 20
        if x >= 500:
            x = 500
    if key_input[pygame.K_DOWN]:
        y += 20
        if y >= 500:
            y = 500
    
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x - 25, y - 25), 25)
    pygame.display.flip()
    clock.tick(60)