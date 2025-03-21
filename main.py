import pygame
from src.components.obstacle.obstacle import obstacles
from src.config import (SCREEN_WIDTH, SCREEN_HEIGHT, FPS)
from src.components.character.character import players

# Inicializa pygame
pygame.init()

# Configuración de pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mi Primer Juego")

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Crear grupo de sprites y añadir todo
all_sprites = pygame.sprite.Group()
all_sprites.add(players, obstacles)

# Bucle principal
running = True
while running:
    clock.tick(FPS)

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar
    all_sprites.update(all_sprites)

    # Dibujar
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    # Actualizar pantalla
    pygame.display.flip()

pygame.quit()
