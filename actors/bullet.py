import pygame

class Bullet:
    def __init__(self, pos: pygame.Vector2, speed: int, radius: int) -> None:
        self.pos: pygame.Vector2 = pygame.Vector2(*pos)
        self.speed: int = speed
        self.radius: int = radius
    
    def draw(self, window: pygame.Surface) -> None:
        pygame.draw.circle(window, (20, 116, 168), self.pos, self.radius)