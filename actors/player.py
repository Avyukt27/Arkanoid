import pygame
from .bullet import Bullet

class Player:
    def __init__(self, pos: pygame.Vector2, speed: int, shoot_timer: int, sprite: pygame.Surface) -> None:
        self.pos: pygame.Vector2 = pygame.Vector2(pos)
        self.speed: int = speed
        self.default_shoot_timer: int = shoot_timer
        self.shoot_timer: int = shoot_timer
        self.sprite: pygame.Surface = sprite
    
    def draw(self, window: pygame.Surface) -> None:
        window.blit(self.sprite, self.pos)
    
    def construct_bullet(self, bullet_list: list[Bullet]) -> None:
        if self.shoot_timer == 0:
            bullet_list.append(Bullet(pygame.Vector2(self.pos.x + self.sprite.get_width() / 2, self.pos.y), self.speed, 10))
            self.shoot_timer = self.default_shoot_timer