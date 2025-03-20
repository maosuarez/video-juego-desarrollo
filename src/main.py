import pygame
from components.Obstacle import Obstacle
from config import (SCREEN_WIDTH, SCREEN_HEIGHT, FPS)
from components.Character import Player

# Inicializa pygame
pygame.init()

# Configuración de pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mi Primer Juego")

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Crear grupo de sprites y añadir el jugador
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
player1 = Player(color=(0, 255, 0),
                 keys={'left': pygame.K_a,
                       'right': pygame.K_d,
                       'jump': pygame.K_w})
player2 = Player(color=(255, 255, 255),
                 keys={'left': pygame.K_LEFT,
                       'right': pygame.K_RIGHT,
                       'jump': pygame.K_UP})
players.add(player1)
all_sprites.add(player1)
players.add(player2)
all_sprites.add(player2)

# Crear obstáculos
obstacles = pygame.sprite.Group()
obstacle1 = Obstacle(300, 400, 100, 20, (255, 0, 0))
obstacles.add(obstacle1)
all_sprites.add(obstacle1)

# Bucle principal
running = True
while running:
    clock.tick(FPS)

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar
    all_sprites.update()
    for player in players:
        player.choque(obstacles.sprites())

    # Dibujar
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    # Actualizar pantalla
    pygame.display.flip()

pygame.quit()
