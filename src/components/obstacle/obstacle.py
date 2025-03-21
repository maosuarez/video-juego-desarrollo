import pygame


# Clase de obstáculo
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


list_obstacles = [
    Obstacle(300, 400, 100, 20, (255, 0, 0)),
    Obstacle(400, 550, 100, 50, (255, 255, 0)),
    Obstacle(550, 500, 60, 100, (0, 255, 255))
]

obstacles = pygame.sprite.Group()
for obstacle in list_obstacles:
    obstacles.add(obstacle)
