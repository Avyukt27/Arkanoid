import pygame
from actors.player import Player

pygame.init()

win_width: int = 500
win_height: int = 500
window: pygame.Surface = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Arkanoid")

fps: int = 30
clock: pygame.time.Clock = pygame.time.Clock()

player_sprite: pygame.Surface = pygame.image.load(r"c:\Users\abhis\OneDrive\Code\Python\Games\Arkanoid\assets\player.png")

def update_screen(window: pygame.Surface) -> None:
    window.fill((0, 0, 0))
    player.draw(window)
    pygame.display.update()

player: Player = Player((win_width // 2, 400), 10, 5, player_sprite)
run: bool = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.pos.x > 0:
        player.pos.x -= player.speed
    if keys[pygame.K_RIGHT] and player.pos.x + player_sprite.get_width() < win_width:
        player.pos.x += player.speed

    update_screen(window)
    clock.tick(fps)

pygame.quit()
exit()