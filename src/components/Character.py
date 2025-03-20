from config import (SCREEN_WIDTH, SCREEN_HEIGHT,
                    PLAYER_WIDTH, PLAYER_HEIGHT)
import pygame
from components.Obstacle import Obstacle


# Clase del Jugador
class Player(pygame.sprite.Sprite):
    def __init__(self, color, keys):
        super().__init__()

        # Forma
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        # Fisica
        self.vel_y = 0
        self.gravity = 1
        self.jump_strength = -15

        # Controles personalizados
        self.keys = keys

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.keys['left']]:
            self.rect.x -= 5
        if keys[self.keys['right']]:
            self.rect.x += 5
        if keys[self.keys['jump']] and self.rect.bottom >= SCREEN_HEIGHT:
            self.jump()

        # Aplicar gravedad
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        # Limitar al suelo
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.vel_y = 0

        # Evitar salir de la pantalla
        self.choque()

    def choque(self, obstacles: list['Obstacle'] = []):
        # Limitar los bordes de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        # Detectar colisión con obstáculos
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                # Si cae encima, se queda parado
                if self.vel_y > 0 and self.rect.bottom >= obstacle.rect.top:
                    self.rect.bottom = obstacle.rect.top
                    self.vel_y = 0

    def jump(self):
        self.vel_y = self.jump_strength
