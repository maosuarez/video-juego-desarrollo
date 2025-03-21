import pygame
import os

# Inicializa Pygame y el mixer
pygame.init()
pygame.mixer.init()

# Construir ruta absoluta desde la raíz del proyecto
base_path = os.path.dirname(
    os.path.abspath(__file__)
    )  # Obtiene la ruta actual de sound.py
sound_path = os.path.join(
    base_path, '..', '..', 'assets', 'sounds', 'jump.wav'
    )  # Sube dos niveles y entra a assets/sounds

# Cargar el sonido
jump_sound = pygame.mixer.Sound(sound_path)
