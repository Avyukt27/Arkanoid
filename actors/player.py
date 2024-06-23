import pygame

class Player:
    def __init__(self, pos: tuple[int, int], speed: int, shoot_timer: int, sprite: pygame.Surface = pygame.Surface((0, 0))) -> None:
        self.pos: pygame.Vector2 = pygame.Vector2(*pos)
        self.speed: int = speed
        self.shoot_timer: int = shoot_timer
        self.sprite: pygame.Surface = sprite
    
    def draw(self, window: pygame.Surface) -> None:
        pygame.draw.rect(window, (255, 0, 0), pygame.Rect(self.pos.x, self.pos.y, 10, 10))