from src.config import (SCREEN_WIDTH, SCREEN_HEIGHT,
                        PLAYER_WIDTH, PLAYER_HEIGHT,
                        GRAVITY, JUMP_STRENGHT,
                        STANDARD_X)
from src.scenes.sound import (jump_sound)
import pygame
from src.components.obstacle.obstacle import Obstacle
from typing import Union


# Clase del Jugador
class Player(pygame.sprite.Sprite):
    def __init__(self, color, keys):
        super().__init__()

        # Tamaño Jugador
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(color)  # Color Jugador
        self.rect = self.image.get_rect()  # Mostrar
        # Renderizar en la mitad de la pantalla
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        # Fisica
        self.vel_y = 0  # Velocidad vertical por defecto
        self.vel_x = 0  # Velocidad horizontal por defecto
        self.gravity = GRAVITY  # Valor de la gravedad
        self.jump_strength = JUMP_STRENGHT  # Potencia del salto
        self.jump_available = True  # ¿Esta permitido el salto?

        # Colisiones

        # Controles personalizados
        self.keys = keys

    def update(self, all_sprites: list[Union['Obstacle', 'Player']] = []):
        self.vel_x = 0
        keys = pygame.key.get_pressed()  # Saber que tecla se presiono
        if keys[self.keys['left']]:
            self.vel_x = -STANDARD_X  # Moverse 5 pixeles a la Izquierda
        if keys[self.keys['right']]:
            self.vel_x = STANDARD_X  # Moverse 5 pixeles a la derecha
        if keys[self.keys['jump']] and self.jump_available:
            self.jump()  # Funcion

        # Movimiento en x (con colisiones)
        self.move_horizontal(all_sprites)

        # Aplicar gravedad
        self.vel_y += self.gravity
        
        # Movimiento en y (con colisiones)
        self.move_vertical(all_sprites)

        # Limitar con la pantalla
        self.bordes()

    def move_horizontal(self, sprites):
        # Aplicar movimiento horizontal
        self.rect.x += self.vel_x
        
        # Verificar colisiones horizontales
        for sprite in sprites:
            # Evitar colisionar consigo mismo
            if sprite == self:
                continue

            # Si hay colisión después de moverse
            if self.rect.colliderect(sprite.rect):
                # Colisión con el mismo tipo (jugador)
                if isinstance(sprite, type(self)):
                    if self.rect.centery == sprite.rect.centery:
                        # Colisión por la derecha
                        if self.vel_x > 0:
                            sprite.rect.left = self.rect.right
                        # Colisión por la izquierda
                        elif self.vel_x < 0:
                            sprite.rect.right = self.rect.left
                        # Si ambos se mueven en direcciones opuestas
                        if self.vel_x == -sprite.vel_x:
                            self.rect.x -= self.vel_x
                
                # Colisión con obstáculo
                elif not isinstance(sprite, type(self)):
                    # Colisión por la derecha
                    if self.vel_x > 0:
                        self.rect.right = sprite.rect.left
                    # Colisión por la izquierda
                    elif self.vel_x < 0:
                        self.rect.left = sprite.rect.right

    def move_vertical(self, sprites):
        # Guardar posición anterior
        old_y = self.rect.y
        
        # Aplicar movimiento vertical
        self.rect.y += self.vel_y
        
        for sprite in sprites:
            # Evitar colisionar consigo mismo
            if sprite == self:
                continue

            # Si hay colisión después de moverse
            if self.rect.colliderect(sprite.rect):
                # Determinar si la colisión es desde arriba o desde abajo
                # Si antes estábamos encima del sprite
                if old_y + self.rect.height <= sprite.rect.y:
                    self.rect.bottom = sprite.rect.top
                    self.vel_y = 0
                    self.jump_available = True
                # Si antes estábamos debajo del sprite (colisión hacia arriba)
                elif old_y >= sprite.rect.y + sprite.rect.height:
                    self.rect.top = sprite.rect.bottom
                    self.vel_y = 1  # Pequeña velocidad hacia abajo para iniciar caída
                # Colisión lateral (ya manejada en move_horizontal)

    def bordes(self):
        # Limitar al suelo
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.vel_y = 0
            self.jump_available = True
        # Limitar el borde izquierdo
        if self.rect.left < 0:
            self.rect.left = 0
        # Limitar el borde derecho
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def jump(self):
        self.vel_y = self.jump_strength
        jump_sound.play()
        self.jump_available = False


list_players = [
    Player(color=(0, 255, 0),
           keys={'left': pygame.K_a,
                 'right': pygame.K_d,
                 'jump': pygame.K_w}),
    Player(color=(0, 0, 255),
           keys={'left': pygame.K_LEFT,
                 'right': pygame.K_RIGHT,
                 'jump': pygame.K_UP})
]

players = pygame.sprite.Group()
for player in list_players:
    players.add(player)