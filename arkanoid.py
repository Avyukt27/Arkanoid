import pygame
from actors.player import Player
from actors.bullet import Bullet

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
    for bullet in bullets:
        bullet.draw(window)
    pygame.display.update()

player: Player = Player(pygame.Vector2(win_width // 2, 400), 10, 10, player_sprite)
bullets: list[Bullet] = []
run: bool = True
while run:
    if player.shoot_timer > 0:
        player.shoot_timer -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()

    # Left Right Movement
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.pos.x > 5:
        player.pos.x -= player.speed
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.pos.x + player_sprite.get_width() + 5 < win_width:
        player.pos.x += player.speed

    # Shooting
    if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
        player.construct_bullet(bullets)
    
    for bullet in bullets:
        bullet.pos.y -= bullet.speed

    update_screen(window)
    clock.tick(fps)

pygame.quit()
exit()