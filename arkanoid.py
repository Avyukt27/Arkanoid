import pygame

pygame.init()

win_width: int = 500
win_height: int = 500
window: pygame.Surface = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Arkanoid")

run: bool = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
exit()