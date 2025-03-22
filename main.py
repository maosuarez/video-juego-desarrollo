import pygame
from src.components.obstacle.obstacle import obstacles
from src.config import (SCREEN_WIDTH, SCREEN_HEIGHT, FPS)
from src.components.character.character import players
from src.scenes.image import load_image

# Inicializa pygame
pygame.init()

# Configuración de pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mi Primer Juego")

# Imagenes

# Cargar imagen de fondo
background = load_image('background.png')
# Ajustar al tamaño de la pantalla
background = pygame.transform.scale(background, (800, 600))

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Crear grupo de sprites y añadir todo
all_sprites = pygame.sprite.Group()
all_sprites.add(players, obstacles)

# Bucle principal
running = True
bg_x = 0
while running:
    clock.tick(FPS)

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pantalla con el fondo
    screen.blit(background, (0, 0))  # Dibujar fondo en la pantalla

    # Actualizar
    all_sprites.update(all_sprites)

    # Dibujar
    all_sprites.draw(screen)

    # Actualizar pantalla
    pygame.display.flip()

pygame.quit()
