Documentación del Proyecto

1. Organización del Proyecto

El proyecto está organizado en la siguiente estructura de carpetas:

VIDEO-JUEGO-SEMILLERO/
│
├── assets/              # Archivos multimedia (sonidos, imágenes, fuentes)
│   ├── fonts/
│   ├── images/
│   └── sounds/
│       └── jump.wav
│
├── docs/                # Documentación del proyecto
│
├── my_env/              # Entorno virtual (si aplica)
│
├── src/                 # Código fuente
│   ├── components/      # Componentes modulares
│   │   ├── character/   # Lógica del personaje
│   │   └── obstacle/    # Lógica de los obstáculos
│   ├── scenes/          # Manejo de escenas
│   └── config.py        # Configuración del juego (FPS, tamaño pantalla, etc.)
│
├── .gitignore           # Archivos y carpetas a excluir en Git
├── main.py              # Archivo principal para ejecutar el juego
└── requirements.txt     # Librerías necesarias para el entorno

Breve explicación de las carpetas clave:

assets/: Contiene los recursos visuales y sonoros usados en el juego.

components/: Dividido en submódulos para organizar el código por tipo de entidad (personajes, obstáculos).

scenes/: Donde se gestionan las escenas, como el sonido.

config.py: Centraliza configuraciones reutilizables.

2. Desglose del Archivo Principal (main.py)

El archivo principal main.py tiene la siguiente estructura:

Importaciones clave

import pygame
from src.components.obstacle.obstacle import obstacles
from src.config import (SCREEN_WIDTH, SCREEN_HEIGHT, FPS)
from src.components.character.character import players

¿Por qué?

Se importa Pygame para controlar la lógica del juego.

Se traen los elementos necesarios: obstáculos, configuraciones y personajes desde los módulos correspondientes.

Configuración de pantalla

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mi Primer Juego")
clock = pygame.time.Clock()

Objetivo:

Inicializa Pygame.

Define el tamaño de pantalla (tomado de config.py).

Controla los FPS mediante un reloj.

Grupo de Sprites

all_sprites = pygame.sprite.Group()
all_sprites.add(players, obstacles)

Función:

Agrupa todos los objetos (jugadores y obstáculos) para actualizarlos y dibujarlos juntos de manera eficiente.

Bucle Principal

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(all_sprites)
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()

🔹 clock.tick(FPS): Controla la velocidad del bucle.
🔹 pygame.event.get(): Captura eventos (por ejemplo, cerrar la ventana).
🔹 update(): Actualiza la lógica de los sprites.
🔹 draw(): Dibuja todos los elementos en la pantalla.
🔹 pygame.display.flip(): Refresca la pantalla completa.

🛠️ Siguientes pasos:

Agregar manejo de colisiones.

Incluir una pantalla de inicio y de game over.

Optimizar la carga de recursos (precargar sonidos e imágenes).