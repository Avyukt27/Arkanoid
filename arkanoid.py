import pygame
from actors.player import Player

pygame.init()

win_width: int = 500
win_height: int = 500
window: pygame.Surface = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Arkanoid")

player: Player = Player((win_width // 2, 300), 5, 5)
run: bool = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    player.draw(window)
    pygame.display.update()

pygame.quit()
exit()